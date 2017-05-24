                        var name = '未命名';
                        var input = document.getElementById('file');

                        input.addEventListener('change', function () {
                            var files = document.getElementById('file').files;
                            var file = files.item(0);
                            name = file.name;
                            var reader = new FileReader();
                            reader.onloadend = function (e, content) {
                                var nlp = JSON.parse(decodeURIComponent(e.target.result));
                                node_slots.value = nlp.origin_slots;
                                node_rules.value = nlp.origin_rules;
                                update();
                            };
                            reader.readAsText(file, 'utf-8');
                        });


                        function Bsg() {

                        }
                        Bsg.prototype = {
                            slots: {},
                            rules: {},
                            checkInputSlots: function (input) {

                                var tips = '';

                                { // 检测非法字符
                                    var pattern = /([^\u4E00-\u9FA5\uF900-\uFA2Da-zA-Z0-9_\s=,\*]+)/g;
                                    var lines = input.split("\n");
                                    for (var k in lines) {
                                        var tmp = lines[k];

                                        while (arr = pattern.exec(tmp)) {
                                            tips += '非法符号: ' + arr[1] + '; 所在行:' + tmp + '\r\n'
                                        }
                                    }
                                }

                                node_tips_slots.innerText = tips;

                            },
                            checkInputRules: function (input) {

                                var tips = '';

                                { // 检测非法字符
                                    var pattern = /([^\u4E00-\u9FA5\uF900-\uFA2Da-zA-Z0-9_\s=,\.<>]+)/g;
                                    var lines = input.split("\n");
                                    for (var k in lines) {
                                        var tmp = lines[k];

                                        while (arr = pattern.exec(tmp)) {
                                            tips += '非法符号: ' + arr[1] + '; 所在行:' + tmp + '\r\n'
                                        }
                                    }
                                }

                                node_tips_rules.innerText = tips;
                            },
                            flushSlots: function (input) {
                                var slots = {};
                                var pat = (/<(.*?)>/g);
                                while (arr = pat.exec(input)) {
                                    if (!slots.hasOwnProperty(arr[1])) {
                                        slots[arr[1]] = ['词条默认值'];
                                    }
                                }

                                var lines = input.split("\n");
                                for (var k in lines) {
                                    var tmp = lines[k];

                                    tmp = tmp.replace("*", ".+");
                                    var arr = (/(\w+)\s*?=\s?(.*)/g).exec(tmp);
                                    if (arr && arr.length >= 3) {
                                        var slotName = arr[1];
                                        var slotValues = arr[2].split(/[\s,]/g);

                                        if (slotValues.length > 0) {
                                            slots[slotName] = [];
                                            for (var m in slotValues) {
                                                if (slotValues[m] && !slots[slotName].hasOwnProperty(slotValues[m])) {
                                                    slots[slotName].push(slotValues[m]);
                                                }
                                            }
                                        }
                                    }
                                }
                                this.slots = slots;
                            },
                            flushRules: function (input) {
                                var lines = input.split("\n");
                                for (var k in lines) {
                                    var li = lines[k];
                                    var arr = (/([\w\.]+)\s*?=\s?(.*)/g).exec(li);
                                    if (arr && arr.length >= 3) {
                                        var ruleKey = arr[1];
                                        if (!this.rules.hasOwnProperty(ruleKey)) {
                                            this.rules[ruleKey] = [];
                                        }
                                        var temp = arr[2].split(/[,]/g);

                                        var slots_for_replace = {};
                                        for (var slot_name in this.slots) {
                                            slots_for_replace['<' + slot_name + '>'] = '(' + this.slots[slot_name].join('|') + ')';
                                        }

                                        for (var j in temp) {
                                            var x = temp[j].trim();

                                            if (x.length > 0) {
                                                var p = x;
                                                var pp = (/<(.+?)>/g);
                                                while (arr = pp.exec(x)) {
                                                    var sk = arr[1];
                                                    var sv = ["未定义信息"];

                                                    if (this.slots[sk]) {
                                                        sv = this.slots[sk];
                                                    }

                                                    var fr = "(" + sv.join("|") + ")";
                                                    p = p.replace(new RegExp(arr[0], 'g'), fr);
                                                }

                                                for (var slot_f_p in slots_for_replace) {
                                                    p.replace(slot_f_p, slots_for_replace[slot_f_p]);
                                                }

                                                var r = {
                                                    origin: x,
                                                    pattern: '^' + p + '$',
                                                    groups: []
                                                }
                                                var wp = /<(.*?)>/g;

                                                while (arr = wp.exec(r.origin)) {
                                                    r.groups.push(arr[1]);
                                                }
                                                r.groups.push();
                                                this.rules[ruleKey].push(r);
                                            }
                                        }
                                    }
                                }
                            },
                            flushGrammar: function () {
                                var gram = '';
                                for (var slot_name in this.slots) {
                                    var arr1 = this.slots[slot_name];
                                    var arr2 = [];
                                    for (var i in arr1) {
                                        if (arr1[i].indexOf('.+') < 0) {
                                            arr2.push(arr1[i]);
                                        }
                                    }

                                    gram += ''
                                            + '<' + slot_name + '> = '
                                            + ((arr2.length > 0) ? arr2.join("| \n") : '词条默认值')
                                            + ";\n";
                                }

                                var ruleWithSlots = [];
                                var ruleWithoutSlots = [];
                                for (var i in this.rules) {
                                    for (var k in             this.rules[i]) {
                                        var n = this.rules[i][k];
                                        var txt = n.origin.trim();
                                        if (txt.indexOf('<') > -1) {
                                            if (txt.length > 0 && !ruleWithSlots.hasOwnProperty(txt)) {
                                                ruleWithSlots.push(txt);
                                            }
                                        } else {
                                            if (txt.length > 0 && !ruleWithoutSlots.hasOwnProperty(txt)) {
                                                ruleWithoutSlots.push(txt);
                                            }
                                        }
                                    }
                                }

                                gram += '<auto_create_node> = ' +
                                        (ruleWithoutSlots.length > 0 ? ruleWithoutSlots.join(' | \n') : '词条默认值' )

                                        + ';\n';


                                gram += '<_wakeup> = 唤醒词占位符;\n';

                                gram += "\n\n_SCENE_ID_ 0\n\n";

                                gram += '( <auto_create_node> )\n\n'
                                gram += '( <_wakeup><auto_create_node> )\n\n'

                                for (var i in ruleWithSlots) {
                                    gram += '( ' + ruleWithSlots[i] + ' )\n';
                                    gram += '( <_wakeup>' + ruleWithSlots[i] + ' )\n';
                                }

                                this.grammar = gram;

                                this.origin_slots = node_slots.value;
                                this.origin_rules = node_rules.value;

                            },
                            flush: function (slotsText, rulesText) {
                                this.slots = {};
                                this.rules = {};
                                this.flushSlots(slotsText);
                                this.flushRules(rulesText);
                                this.flushGrammar(slotsText, rulesText);
                            }
                        }

                        var nlp = new Bsg();
                        nlp.version = "0.1";
                        function testInput() {
                            console.log(node_test.value);
                            node_info.innerText = "";

                            var test_result_1 = []; // 精确结果
                            var test_result_2 = []; // 非精确结果
                            var keyword = node_test.value.trim();

                            for (var i in nlp.rules) {

                                for (var j in nlp.rules[i]) {
                                    var tmp = nlp.rules[i][j];
                                    var ptn = new RegExp(tmp.pattern);
                                    var arr = ptn.exec(keyword);
                                    if (arr) {
                                        var _domain = i;
                                        var _intent = i;
                                        var _di = i.split('.');
                                        _domain = _di[0];
                                        if (_di.length >= 2) {
                                            _intent = _di[1];
                                        }
                                        var result = {
                                            domain: _domain,
                                            intent: _intent,
                                            object: {}
                                        }
                                        for (var k = 1; k < arr.length; k++) {
                                            result.object[tmp.groups[k - 1]] = arr[k];
                                        }

                                        if (tmp.pattern.indexOf('*') > -1) {
                                            test_result_2.push(result);
                                        } else {
                                            test_result_1.push(result);
                                        }

                                        console.log(i + '->' + tmp.origin + ' ' + JSON.stringify(result));
                                    }
                                }
                            }

                            results = ([]).concat(test_result_1, test_result_2);

                            var fr = {
                                raw_text: keyword,
                                parsed_text: keyword,
                                results: ([]).concat(test_result_1, test_result_2),
                            };


                            if (results.length > 0) {
                                node_info.innerText = JSON.stringify(fr, null, 4);
                            } else {
                                node_info.innerText = '没有匹配的说法, 请修改词条 规则 或 测试内容';
                            }
                        }

                        function update() {
                            nlp.flush(node_slots.value, node_rules.value);

                            grammar_source.value = nlp.grammar;
                            link_save_rule.href = URL.createObjectURL(new Blob([encodeURIComponent(JSON.stringify(nlp, null, '    '))], {type: "text/plain"}));


                            testInput();
                            console.log(JSON.stringify(nlp, null, 4));
                        }

                        node_slots.oninput = function () {
                            nlp.checkInputSlots(node_slots.value);
                            update();
                        };
                        node_rules.oninput = function () {
                            nlp.checkInputRules(node_rules.value);
                            update();
                        };
                        ;
                        update();

                        node_test.oninput = testInput;
