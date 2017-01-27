#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
import itertools

ALPHABET_S = (
'的一是不在人有我这中大上国来和会到年时们地以要你就下也对道生可能行子得'
'过自之成日多公那天作方都而小好前经然分现心动还业看事学用去月进场力市将'
'主本高如手所长法起她全定与其最点部新者但理第间工实比已关想体重情意此员'
'无身三很从加等些两明名次机金样资内美外因区头文通利位知目民正被队司赛己'
'入元老问平度相特期提女及电安车报十斯化二建应什政东性信把门展海更话又保'
'见水果给股让声品由北气运口尔数儿受活务做任联交常路军真山记再议总至代少'
'基四计感立使接强先题物走今南处马直持管世王各色量该解原风认组太设指非城'
'眼结张笑师收达网拉何神书放德或决光程房影传住投式白告商难件却变示华院带'
'京调近完快每科社边亚界选转五空求增听觉号取便流火爱际项服约权士规奥林连'
'反候集步领委专清条单乐费息办像始续未统级整死首视需深花支共观论必形则导'
'客州李孩改许容吧消言节易命足请势怎即案标备亲江造况育包轻省失往府根站微'
'精百济义越青且米份推低红阿技巴双算满随飞思半企友离石功男源片远供星创显'
'灾具较吗龙校落英称击响治维预型武举字限早段类官音营跟吃兰终质图医银施速'
'值刚语排热切环叫象虽率断找协超呢希震突啊紧除险黑识晚责引装优艺奇款古试'
'研喜伤脸黄尼曾境令够底欢存似争救态护仅防景留究油职六卡继居积兴料乎宝列'
'福八史河杀病农兵季酒香另习负票拿刻织钱铁待送园练楼依破族亿哈仍购招旅益'
'陈土冷评衣停村县食严属朝承川倒初刘错模班帮急按害器店销父围惊般纳牌监洲'
'诉七普配湖左写哥担派止波春谢母故纪欧威血细控室层验域警财若哪均售独攻甚'
'九谁怕竟素训右谈降密讯讲妈港压博闻汉剧状否午玉剑充执皇露额养久审弟静括'
'雷阵您律灵差融涨副临券例富夜短杨简善察守拍苦免舞宣雪批幅略丽激章某索伊'
'脚朋木帝假介减坚航亮退编轮遇康货味届印昨疑换皮歌健沙读秘草圣异顾挥秀冠'
'姐播礼藏尚测句追跌雨顿敢补登跑穿童择块判脑掌沉慢迎怪良革田顺贵怀堂抗付'
'媒课移玩套梦毛夏庭禁肯楚稳央街忙劳卖败陆汽材乡检永射韩宗烈互齐享吸版宫'
'岛乱痛树束森透吉兄妇毒赶培丝诺塞犯戏迷散申顶莫喝恐罪危访庆既冰魔掉毕缺'
'援洛靠笔弹唐爷孙虑缓智船拥牙渐雅婚含讨恩述肉萨跳牛伯塔休厅附阶典摇迪鲁'
'忽努君刀餐封促刺竞归饭暴嘴赵损狐码淡佳绍币软勒伦默屋丹输雄敌寻尤盟梅抓'
'耳摄析泰贝荣洋探逐睡疗湾瑞姑络措蓝架吴鱼盛熟阴隐抢递浪序弱捐夺估徐董盖'
'睛纷延醒避庄秦础甲鲜毫库曼杂释瓦载寒旧频尊莱爸丁遗授闪握菜予误献概障坏'
'唯挑钢幕姓姆桥忍珠妹距遭伴虎润唱亦辆亡订鼓贷骨悉询忘狂坦晓趣逃怒箭茶鬼'
'替锋纸篮俄祖扩凯啦宇聚词虚爆麦杜裁召综灯乘诸遍督朗津偏勇惠伟洞宜乌截郑'
'旗固途混贸弃眉诗仪凡侧猛拜伸厚豪涉残贴洗敬菲键谓骑末迅硬隆摩圆紫晨臣署'
'债映励宋泽呀锦零劲诚艾恢符妻违抽弄蒂凤闭宽缩滑俱奔染租炬触罚纯腿徒嘉奋'
'厉筹窗粉柔暂漫疾萧帅刑赏哦横埃舒岸巧哭澳迫赢腾烧灭懂宾郭泪袋粮驾倍戴煤'
'凭敏返饮拔辈缘丈胸蛋潜趋忠魂婆泉氏镜仁潮详宏洪饰烦惯矿桌谋阻聘跃甘惜伍'
'辛娜拳祝吨洁挺搭悲柳迟焦叔郎贫搞昌患盈尾恨尖沿彻赔龄孔摸羽储墨珍忆腰肩'
'冒殿喊档废廷衡番狗黎侯陷幼鸟圳隔驻犹竹陪扫燃邦辑堡孤壁拟狠弗殊箱凝乔振'
'览奉稍奏汗赫玛偶贡绪纵灰撞卢玄姚兼邀绕汤忧晋侵帕植罢荷辉琴拒册倾慧桑浓'
'裂肥寺沟籍扶池俗炸袭坡宿浮曰伏篇秒晶皆壮岗熊繁跨锁碎狼呈驶滚胆偿疯仔液'
'慕沃泥旋赖宅誉仓飘颗辞恋凉爵邮赴魏彼陵惨贯奈撑扑肤羊兽幽瞬霍拖薄谨芳慎'
'赠捷嘛漂穆棒乏穷翼尘幻浙貌祥瞧渡踪巡吓寿臂孟迁磨肃匹慈披荒耶吹帐韦赤耐'
'铜蹈挡娃猜骗吐猫恒曹翔仰页描聊汶阁丢亏胀舰允脉悄甜涛粗踏咬绘娇傅鞋莲侠'
'鹏侍怖恰迈娱鹿榜怨刊塑拓扰抚慰辽廉缔牵吕朵鼻滋鸣颇堆唇莉妖邪撤扭仲役拨'
'炎惑疆捕胁厦募卓琳戈苍莎崇鸿遥猪碍邓浦泡绵滨棋疼盗垂桃杭贾戒遵盾轰愤爬'
'冯糖哼嫌胞皱埋躲嘿瓜稿贺姿袁滴悬译奴辰牢芒掩艰忌辅醉狱逆雾柱柏肌擦添丧'
'梯傲乳畅惧椅俩扮苗抖辖贤斤贼薪庙屏填哀驱旨氛抛堪蛇践慌腹邻颤悠穴桂妮枝'
'酷宪沪怜屈晃碧昏庞撒嗯恭烂携彭郡遣揭哲蒋吟徽霸履刷躺聪喷爹辩悟盯腐匆傻'
'闷劝疲搬挤矛弯牧夹祭劫胖芬浑轨翰旺斜葛拆循陕孝墓玲寄逊械踢渠剂挖岂肚霞'
'锅疫潘葡吻抑纹淘栏翠瘦疏纠诊浅裤枚逸脆肖岭框漠伐鹰虹驰欠炭厌颁赚缴谐吞'
'炒睁豫蔡挣欺涵寨毅帆押稀敲爽萄盐痕泳胎歧璃玻舌寂阔勃诱割峡瞪辣碗倡僧卿'
'猎羞赌祸悔抹冻唤拦蜜漏叛厨契柴轿轩缠歉衫芝缝恼晴崔塌廊勾遂赋掘鼠逢帽嫁'
'姬啸锡咖纲怔孕谦铭乙霜嫩拾熙笼闯齿亭串憾夕汪鼎膀蜂魅茨舟滩屁湘摘啥茫辱'
'衰刹仗趁琼昭吼肠诞糕讶斩捧涯饱袍摊裕吾愣削栋妥婴啡堵粒罩篷攀扇盒骤殖坊'
'赐妃寓胶乖贪桶狮掠跪枫艇晕惹佐瑟蛮砸饿韵扔窝姻渴催谊葬丛崩柯丫歇喘绳旭'
'摔薇碑硕眠氧渔脂妨盆裙蓄蕾薛怡浴砍捉盼妳劣靖颈贩宠勉弘萍亨愁斥畏罕斌喃'
'厢洒凑谱斑泊愉谅坤牲懒陌囊兆淮彦媚誓鹤惟臭逝铃躯棉谭叉侦挪膝骄姨脖巾亩'
'挫遮甸艘鲍吵婷琪垃灌堰圾姊胃尉烤翁颖禅柄惩剪蝶荆宛屠函渊溃尿滞陛拘詹绑'
'坝溢淋擅寇煌剥儒鞭腔汰漆猴腕宙瑶饼冈辨肝夷卑秩弓帖逻冥诏麟郊隶慨叠饶崖'
'矮甫瓷坎蓬苑乒贞肿刃衷膜巷馨搏巫愚癌缅巢墅砖耕哎盲锻塘脾颠膨茅捏咐宰骚'
'尹纱婉眸珊裹晖撕轴诈祈耻汁萌昔瑜潭莹菌竭雀楠劈庸邵喉矣勿卒尬舱尴凰枯煞'
'咳蓉魄峻坠屡抄狄趟耸眨钦衍侨窃撼咒喀棍伽陀瞒牺吏玫讼哇杉甩乞掀哑樱沫踩'
'筒奢躁煮肢爪沾铝粹朕坪龟浸瞳谎顽诡灿豹窄衬笨逾呜墟菊匪瑰澜杖磁耍喻蒸娟'
'彰暑肆泼舅裴兔邱淑啤昊拱磊壶垫泣腻鸭骇芦陡奎翅妄寡娶蔬吩擎岚逛棚纺镖狭'
'俞耿冤嘲歪逗禄黛彬烛萝钉骏犬鹅沧匠棵颊芙潇匙株杏睹暨螺舆恍倩揉虾垒虐扳'
'脊碌辜滕贱雍逮桐隙涅嫂卸瞎鑫悍屯莞噢裔侣涩巩稻霆栖俏跆滥诀熬贬蹲曝畜哟'
'哩哨襄拂碳羡畔赈枢皓浆丞囚蜀嘱匈沐枕宵酱敞栽擒雯倘伞讽渗梨嗓倦摧咕钓焉'
'翎喇聂棺屿躬魁蒲揽澡删愕彪镑粤搂郝诵惶顷廖绽钧奠叮嫣弊窜捡粘烁沸梳铸晌'
'桩酿搁奕冕寞肾湛诧娅膊嚷焚俺坟拢砂喔凸鸦赎阎壤痒屑啪媳虞桓烫兮醇丙绎呐'
'燥霉淳仕骆倚驼赁捞藩旱蔽蔓朔晏辐玮敛琦趴斋斐卦矶勘芭禹傍倏禽蹄厮汝祷渝'
'媛乓缕坞阐绸悼垮嘶椒兜凛俘芯秉焕阮笛搅跋垄鄙毯耽黯蓦冶膏瀑恳贿朽迄寝碟'
'逍飙驴窟栈茵邹瞥尧斧菩槽歹匀祁棠翘懈萎凳妾咧蛛洽丐禀昧蕊稽颂妒恕梭忖腥'
'怯乍蟹砰暮隧霖谜衙淹牡撇旷冀缸瘤掷庚臀埔祀徙牠溶蔚惕婢姥灼豁稚暇铅霄嚣'
'瞄鄂肇巅纬戳邢冉虏倪妍崛煎沛磅噬蚀诛嘎粥陋秃韧惫卵窑邑浏茄咏呻咋妞腺茹'
'嗣樊莽涡彤芽澈绮舔窥唔厥妓弧瘾裳瓣帜蚁拯醋嘟闽毙哉绒僚龚汹甄筝鞍滔槛阜'
'窦呃琉茜谴剔酋胤膛沦葫琢遏枉嵩橙咪敷渣枣梵溅赦蝴匿橡榻挠狡瘫叱挟磋敖嵌'
'绅巍迦绰侃磕襟峨伺晔矢嫉髓泻剖遁帷堕蹦肪硫棕娥钞祠酌讳韶熄饲侮琐靴翩袜'
'挚觅哮瞩犀叨嗨侈蚊渺僻酥鳞檀庇闸牟汀泌珀揣铮絮昼揪嗡咦孽猿禧陇闺浇搓孜'
'嘘柬亥憋睐吱沮沽肘钮盎棘梧拙沁瞻矫拭筷嗦俭谕慑眷拽蝉靡嗅廓寥禾葵炳绞淌'
'睫嗽锌翡鲸绯羌怠颐淇嚼眶咙窍朦辕噩慷舜寅盔肋梓狞叩弩簿锣掐靓鸽茎舶胧缀'
'庶凹疚噗笙颅栅扒虔呕浔莺瑾汕晤惭拌赣谍戛缆缪炯蒜缉譬畴沼楷芜璋戮婿蚕炽'
'阱蛙弈菁槐匕滤嗤烹诠伶筛氯浊眩裘蕃咚芷拇鞠凿蹭蝎佟璧驿岔沌黏聆璐椎狈拧'
'啧曙榆梢渭藻榄芹邸褐啼疤礁橘舵殴黔瑛撩聋钰懿嬴猩屎汛竿绢蛟叟苛窒癸歼拎'
'溺寰兢峭叭簇喽鳍刁咆屹瑚鞘麒菇氓雌蹙娄徘阀勺佬觑竣崭鹃戎谬卉荧绚氨逞瞅'
'窘篆攒哆嚎诫蚂驭稣鲨笃骸陨膳粪岑蛊楞榴睦擂烘憎町匣讥箫蕉橄臻戊戟嗜斟饺'
'蝇氢嬉绫罡澎婶壹粟迸恬岐抿蜘惚翟绊嘀蝠袱漩捅垣奚攸忿唾吭珂壬煽珑腮渤糙'
'滇霎跄橱啃卯诣踉俨悯邯漳锯嗔咎芮烨惮笋苯亢璞麓诅猾鸾晦驯苇扼宦揍鲤巳籁'
'趾秽砚汾辙瀚炙辫琛坍洼敝抒竺悚濒缭蹬讪硝沂噜濮烯漱犁姗缎拣讷铎羁霾踝赂'
'烙莆褚峙俐穹茗孚钙驹婪侥萱瑕倔疹椰钝靳萃酉哧阙荔钗绥戌垦辄恃暧髅茉毓辗'
'梗熔祯懊玺嬷飓馅砌骷钾褪郅哽炜疮呛锥啰栩哒焱猝癫霹懦祺汲痘墩棣窖唬紊腑'
'雳揖昕蟒泸铠羹洱狩玖蝙缤潍璨桦黝坂璀羲晟悸麾柠搀纶踱颔轧枭柿祟殆炖渎敕'
'檬冢沥狰韬埠傀馒弼酣葆筠惬葎恙桨咄熠邡妩憨袂琶瞟雏搐萤酵闫亟忡皙帛槟痪'
'蠕唠涟憧蛤髯憬浣骼剌踹跺煜弛诬涤孵稼篱跻榕跷涧籽琵炕鬓褒吝桀呗稷跤佼狙'
'吮靶筐樟叽拷屉倭怅脯殉荀蓓惺郸稠垢孰湃恪奄泾簧甬锵皖掺咀邃嫡摹痊囤蒿淤'
'宸悴翌恺瑙偎秤噶喵谒淄亵酶儡懵劾荃掣炊馀蔼髦暄憔鹊胺峪蹿蜒玑怦掳睬惋笠'
'嫔昱鸠飒茸渍攘镀隘呱曜婕瞰惘衲酪嚓郴绛挝遐抉戍栓骋铂肮隅迥皋蹊烽峦撮镐'
'淼疙谧壑矗痰蕙猥樵渲匮昵岱泵骁簌榈卞胥鸳殡瘩迂呸唧荼歆瘟膺泓胯蜿惦砾咫'
'漉嗒躇煦忑饷矜嗖骡漪阖忐喳蘑悖踌茧伎虬扈萦寐涎俟拴嘈掖搔赘坯啜糯俪呦碾'
'崽瞿蚌饪杞鹭隽忻汐谤钛钊瓢铐镯胚蔷褥骥脐诲羚琥铿芋畸篡偕毡鸯浒莘淆掰迢'
'汴芥吆轶撬鸥岷蚩悻禺婧饵簸捺髻颉鹦笺泗坷拗缨圃忒殇冽嗷菠踞岌氟攥贮凋灞'
'幌洙谛蔗壕筏眈癖蜗唰媲荤惰潺抡秧潼踵濑缮贻殃蹑氮逅邬戾溉粱貂锭疵邂瀛馋'
'砲荟霏蓟袒笈疟臧甥昀纂鹉釉孺釜袄兖迳獒晾筵篝侗俸忏偌恻湄肛喋磐蛾侬茬镁'
'箍褂罹燎鹫丕诽佯俑斓嵋哝钠挛翊螂苞夙煲邺辍锄烬楣鞑蜥痉睽烷藕祐螃猖褶峥'
'昙瘸芊剁婺噎宕苓潞抠镍熹夯椿簪嫖粑斡蘸嫦摒鬟抨颌礴雹衢畿涪钒唆谟贲娓皑'
'珞涓栾啬灸瘪洵憩聿覃祉蝗叼舷窿蜈婊擢琰偃靥驸诃阑炀羔幔旌吠莅涝砺耘椭沅'
'啄伫漕溥铀柚缜驮娩腆沱忱皎恣渥慵甭鞅霁腋桢茱瞠谙潢掂蟾轲轼捎酮弋蟆喆腼'
'诶汞囔浐逵遴睨喏桅锚惴辘涣葩铛峒颍酯骊娼腓遽祚裱馥榭锢侏槌唏昶飕苻姣痞'
'胰檄濡鲲寮霭脓谚蹋崧黜佰闰泠妊灏粕涮湮蕨枷汩鄱珪馍怂箕蹂噤捋磺斛娆玥泞'
'纣蔺娠贰疱琬躏奂鲈邨罂琨溟杵岖匝呎罔醺绶潦撅醛恸萼惆祗啷惿晗韭晁帚衮馁'
'淅澹妪槿缄讹蛰禛糜睑铬闾拄赡赊癞犊钜钼琌翦诩臆豺郜燮铢蟠佘罄裆阉疡骧蚣'
'缥谑骠撂蹒俾跚魇缈柑舫诘羯粲舖䡎葙垠秆郢颚跛碉瞌镂淬咻璟瞑珅妲耆仞珩攫'
'枸嚏湍嵘嚅铉摁薨囡弑塾骜臼蚤篓蜓鲛焙痣掬珣隼垩牒梆诋饕酗唷锺杳徨泯蜻暹'
'觊龛粼邝犷濠啐虢诟挎臾翱盅撵臊傣垛蹴坳羿庾皿秸黠嗫哂螳骐帧娣溴唁鱿琏顼'
'谄烃谲纨獠鳗娑芍藐祂帼醚觎绾锂咿嘤恿赟睢焘厩焖骰姝迩渚碘崆鸢擞谗婀诰砥'
'鼾珈銮阚锰纥夔堑佥缙阂喟笆缇淖锹佗颢岫咂榔珺嗟盹剽涔谯懋桧瘴玷匍窈裨谩'
'腩黍觐荻怆弁苒玘咛癣痫诙猬搪匐旖辇蜃厝淞餮瘀颀宥氤菏嘭啾艮宓遛鳅陂虱玟'
'喱柩涿摞倌劭豌滦蔻荭噱圩揩盂舀榷邕噔旎隍佃酚窕辎楹佞璜茁箔皈怏獗胴饽胱'
'蚓嗳瓒裟亳荥坨剐犒倜漯箴藓蜴恁郦赧娲绡骅袤僮雉咩栎椁蠡谆噫挲酰瘠麝婵邛'
'纭茴爻舐镳琮胫鏖啻熨靼噙邋殒佚挞嗲蹶龌葏泱篪旻耷瞇颦毂姒喙猕闩撸饬瓯孪'
'驷')

ALPHABET_T = (
'的一是不在人有我這中大上國來和會到年時們地以要你就下也對道生可能行子得'
'過自之成日多公那天作方都而小好前經然分現心動還業看事學用去月進場力市將'
'主本高如手所長法起她全定與其最點部新者但理第間工實比已關想體重情意此員'
'無身三很從加等些兩明名次機金樣資內美外因區頭文通利位知目民正被隊司賽己'
'入元老問平度相特期提女及電安車報十斯化二建應什政東性信把門展海更話又保'
'見水果給股讓聲品由北氣運口爾數兒受活務做任聯交常路軍真山記再議總至代少'
'基四計感立使接強先題物走今南處馬直持管世王各色量該解原風認組太設指非城'
'眼結張笑師收達網拉何神書放德或決光程房影傳住投式白告商難件卻變示華院帶'
'京調近完快每科社邊亞界選轉五空求增聽覺號取便流火愛際項服約權士規奧林連'
'反候集步領委專清條單樂費息辦像始續未統級整死首視需深花支共觀論必形則導'
'客州李孩改許容吧消言節易命足請勢怎即案標備親江造況育包輕省失往府根站微'
'精百濟義越青且米份推低紅阿技巴雙算滿隨飛思半企友離石功男源片遠供星創顯'
'災具較嗎龍校落英稱擊響治維預型武舉字限早段類官音營跟吃蘭終質圖醫銀施速'
'值剛語排熱切環叫象雖率斷找協超呢希震突啊緊除險黑識晚責引裝優藝奇款古試'
'研喜傷臉黃尼曾境令夠底歡存似爭救態護僅防景留究油職六卡繼居積興料乎寶列'
'福八史河殺病農兵季酒香另習負票拿刻織錢鐵待送園練樓依破族億哈仍購招旅益'
'陳土冷評衣停村縣食嚴屬朝承川倒初劉錯模班幫急按害器店銷父圍驚般納牌監洲'
'訴七普配湖左寫哥擔派止波春謝母故紀歐威血細控室層驗域警財若哪均售獨攻甚'
'九誰怕竟素訓右談降密訊講媽港壓博聞漢劇狀否午玉劍充執皇露額養久審弟靜括'
'雷陣您律靈差融漲副臨券例富夜短楊簡善察守拍苦免舞宣雪批幅略麗激章某索伊'
'腳朋木帝假介減堅航亮退編輪遇康貨味屆印昨疑換皮歌健沙讀祕草聖異顧揮秀冠'
'姐播禮藏尚測句追跌雨頓敢補登跑穿童擇塊判腦掌沉慢迎怪良革田順貴懷堂抗付'
'媒課移玩套夢毛夏庭禁肯楚穩央街忙勞賣敗陸汽材鄉檢永射韓宗烈互齊享吸版宮'
'島亂痛樹束森透吉兄婦毒趕培絲諾塞犯戲迷散申頂莫喝恐罪危訪慶既冰魔掉畢缺'
'援洛靠筆彈唐爺孫慮緩智船擁牙漸雅婚含討恩述肉薩跳牛伯塔休廳附階典搖迪魯'
'忽努君刀餐封促刺競歸飯暴嘴趙損狐碼淡佳紹幣軟勒倫默屋丹輸雄敵尋尤盟梅抓'
'耳攝析泰貝榮洋探逐睡療灣瑞姑絡措藍架吳魚盛熟陰隱搶遞浪序弱捐奪估徐董蓋'
'睛紛延醒避莊秦礎甲鮮毫庫曼雜釋瓦載寒舊頻尊萊爸丁遺授閃握菜予誤獻概障壞'
'唯挑鋼幕姓姆橋忍珠妹距遭伴虎潤唱亦輛亡訂鼓貸骨悉詢忘狂坦曉趣逃怒箭茶鬼'
'替鋒紙籃俄祖擴凱啦宇聚詞虛爆麥杜裁召綜燈乘諸遍督朗津偏勇惠偉洞宜烏截鄭'
'旗固途混貿棄眉詩儀凡側猛拜伸厚豪涉殘貼洗敬菲鍵謂騎末迅硬隆摩圓紫晨臣署'
'債映勵宋澤呀錦零勁誠艾恢符妻違抽弄蒂鳳閉寬縮滑俱奔染租炬觸罰純腿徒嘉奮'
'厲籌窗粉柔暫漫疾蕭帥刑賞哦橫埃舒岸巧哭澳迫贏騰燒滅懂賓郭淚袋糧駕倍戴煤'
'憑敏返飲拔輩緣丈胸蛋潛趨忠魂婆泉氏鏡仁潮詳宏洪飾煩慣礦桌謀阻聘躍甘惜伍'
'辛娜拳祝噸潔挺搭悲柳遲焦叔郎貧搞昌患盈尾恨尖沿徹賠齡孔摸羽儲墨珍憶腰肩'
'冒殿喊檔廢廷衡番狗黎侯陷幼鳥圳隔駐猶竹陪掃燃邦輯堡孤壁擬狠弗殊箱凝喬振'
'覽奉稍奏汗赫瑪偶貢緒縱灰撞盧玄姚兼邀繞湯憂晉侵帕植罷荷輝琴拒冊傾慧桑濃'
'裂肥寺溝籍扶池俗炸襲坡宿浮曰伏篇秒晶皆壯崗熊繁跨鎖碎狼呈駛滾膽償瘋仔液'
'慕沃泥旋賴宅譽倉飄顆辭戀涼爵郵赴魏彼陵慘貫奈撐撲膚羊獸幽瞬霍拖薄謹芳慎'
'贈捷嘛漂穆棒乏窮翼塵幻浙貌祥瞧渡蹤巡嚇壽臂孟遷磨肅匹慈披荒耶吹帳韋赤耐'
'銅蹈擋娃猜騙吐貓恆曹翔仰頁描聊汶閣丟虧脹艦允脈悄甜濤粗踏咬繪嬌傅鞋蓮俠'
'鵬侍怖恰邁娛鹿榜怨刊塑拓擾撫慰遼廉締牽呂朵鼻滋鳴頗堆脣莉妖邪撤扭仲役撥'
'炎惑疆捕脅廈募卓琳戈蒼莎崇鴻遙豬礙鄧浦泡綿濱棋疼盜垂桃杭賈戒遵盾轟憤爬'
'馮糖哼嫌胞皺埋躲嘿瓜稿賀姿袁滴懸譯奴辰牢芒掩艱忌輔醉獄逆霧柱柏肌擦添喪'
'梯傲乳暢懼椅倆扮苗抖轄賢斤賊薪廟屏填哀驅旨氛拋堪蛇踐慌腹鄰顫悠穴桂妮枝'
'酷憲滬憐屈晃碧昏龐撒嗯恭爛攜彭郡遣揭哲蔣吟徽霸履刷躺聰噴爹辯悟盯腐匆傻'
'悶勸疲搬擠矛彎牧夾祭劫胖芬渾軌翰旺斜葛拆循陝孝墓玲寄遜械踢渠劑挖豈肚霞'
'鍋疫潘葡吻抑紋淘欄翠瘦疏糾診淺褲枚逸脆肖嶺框漠伐鷹虹馳欠炭厭頒賺繳諧吞'
'炒睜豫蔡掙欺涵寨毅帆押稀敲爽萄鹽痕泳胎歧璃玻舌寂闊勃誘割峽瞪辣碗倡僧卿'
'獵羞賭禍悔抹凍喚攔蜜漏叛廚契柴轎軒纏歉衫芝縫惱晴崔塌廊勾遂賦掘鼠逢帽嫁'
'姬嘯錫咖綱怔孕謙銘乙霜嫩拾熙籠闖齒亭串憾夕汪鼎膀蜂魅茨舟灘屁湘摘啥茫辱'
'衰剎仗趁瓊昭吼腸誕糕訝斬捧涯飽袍攤裕吾愣削棟妥嬰啡堵粒罩篷攀扇盒驟殖坊'
'賜妃寓膠乖貪桶獅掠跪楓艇暈惹佐瑟蠻砸餓韻扔窩姻渴催誼葬叢崩柯丫歇喘繩旭'
'摔薇碑碩眠氧漁脂妨盆裙蓄蕾薛怡浴砍捉盼妳劣靖頸販寵勉弘萍亨愁斥畏罕斌喃'
'廂灑湊譜斑泊愉諒坤牲懶陌囊兆淮彥媚誓鶴惟臭逝鈴軀棉譚叉偵挪膝驕姨脖巾畝'
'挫遮甸艘鮑吵婷琪垃灌堰圾姊胃尉烤翁穎禪柄懲剪蝶荊宛屠函淵潰尿滯陛拘詹綁'
'壩溢淋擅寇煌剝儒鞭腔汰漆猴腕宙瑤餅岡辨肝夷卑秩弓帖邏冥詔麟郊隸慨疊饒崖'
'矮甫瓷坎蓬苑乒貞腫刃衷膜巷馨搏巫愚癌緬巢墅磚耕哎盲鍛塘脾顛膨茅捏咐宰騷'
'尹紗婉眸珊裹暉撕軸詐祈恥汁萌昔瑜潭瑩菌竭雀楠劈庸邵喉矣勿卒尬艙尷凰枯煞'
'咳蓉魄峻墜屢抄狄趟聳眨欽衍僑竊撼咒喀棍伽陀瞞犧吏玫訟哇杉甩乞掀啞櫻沫踩'
'筒奢躁煮肢爪沾鋁粹朕坪龜浸瞳謊頑詭燦豹窄襯笨逾嗚墟菊匪瑰瀾杖磁耍喻蒸娟'
'彰暑肆潑舅裴兔邱淑啤昊拱磊壺墊泣膩鴨駭蘆陡奎翅妄寡娶蔬吩擎嵐逛棚紡鏢狹'
'俞耿冤嘲歪逗祿黛彬燭蘿釘駿犬鵝滄匠棵頰芙瀟匙株杏睹暨螺輿恍倩揉蝦壘虐扳'
'脊碌辜滕賤雍逮桐隙涅嫂卸瞎鑫悍屯莞噢裔侶澀鞏稻霆棲俏跆濫訣熬貶蹲曝畜喲'
'哩哨襄拂碳羨畔賑樞皓漿丞囚蜀囑匈沐枕宵醬敞栽擒雯倘傘諷滲梨嗓倦摧咕釣焉'
'翎喇聶棺嶼躬魁蒲攬澡刪愕彪鎊粵摟郝誦惶頃廖綻鈞奠叮嫣弊竄撿粘爍沸梳鑄晌'
'樁釀擱奕冕寞腎湛詫婭膊嚷焚俺墳攏砂喔凸鴉贖閻壤癢屑啪媳虞桓燙兮醇丙繹吶'
'燥黴淳仕駱倚駝賃撈藩旱蔽蔓朔晏輻瑋斂琦趴齋斐卦磯勘芭禹傍倏禽蹄廝汝禱渝'
'媛乓縷塢闡綢悼垮嘶椒兜凜俘芯秉煥阮笛攪跋壟鄙毯耽黯驀冶膏瀑懇賄朽迄寢碟'
'逍飆驢窟棧茵鄒瞥堯斧菩槽歹勻祁棠翹懈萎凳妾咧蛛洽丐稟昧蕊稽頌妒恕梭忖腥'
'怯乍蟹砰暮隧霖謎衙淹牡撇曠冀缸瘤擲庚臀埔祀徙牠溶蔚惕婢姥灼豁稚暇鉛霄囂'
'瞄鄂肇巔緯戳邢冉虜倪妍崛煎沛磅噬蝕誅嘎粥陋禿韌憊卵窯邑瀏茄詠呻咋妞腺茹'
'嗣樊莽渦彤芽澈綺舔窺唔厥妓弧癮裳瓣幟蟻拯醋嘟閩斃哉絨僚龔洶甄箏鞍滔檻阜'
'竇呃琉茜譴剔酋胤膛淪葫琢遏枉嵩橙咪敷渣棗梵濺赦蝴匿橡榻撓狡癱叱挾磋敖嵌'
'紳巍迦綽侃磕襟峨伺曄矢嫉髓瀉剖遁帷墮蹦肪硫棕娥鈔祠酌諱韶熄飼侮瑣靴翩襪'
'摯覓哮矚犀叨嗨侈蚊渺僻酥鱗檀庇閘牟汀泌珀揣錚絮晝揪嗡咦孽猿禧隴閨澆搓孜'
'噓柬亥憋睞吱沮沽肘鈕盎棘梧拙沁瞻矯拭筷嗦儉諭懾眷拽蟬靡嗅廓寥禾葵炳絞淌'
'睫嗽鋅翡鯨緋羌怠頤淇嚼眶嚨竅朦轅噩慷舜寅盔肋梓獰叩弩簿鑼掐靚鴿莖舶朧綴'
'庶凹疚噗笙顱柵扒虔嘔潯鶯瑾汕晤慚拌贛諜戛纜繆炯蒜緝譬疇沼楷蕪璋戮婿蠶熾'
'阱蛙弈菁槐匕濾嗤烹詮伶篩氯濁眩裘蕃咚芷拇鞠鑿蹭蠍佟璧驛岔沌黏聆璐椎狽擰'
'嘖曙榆梢渭藻欖芹邸褐啼疤礁橘舵毆黔瑛撩聾鈺懿嬴猩屎汛竿絹蛟叟苛窒癸殲拎'
'溺寰兢峭叭簇嘍鰭刁咆屹瑚鞘麒菇氓雌蹙婁徘閥勺佬覷竣嶄鵑戎謬卉熒絢氨逞瞅'
'窘篆攢哆嚎誡螞馭穌鯊篤骸隕膳糞岑蠱楞榴睦擂烘憎町匣譏簫蕉橄臻戊戟嗜斟餃'
'蠅氫嬉綾罡澎嬸壹粟迸恬岐抿蜘惚翟絆嘀蝠袱漩捅垣奚攸忿唾吭珂壬煽瓏腮渤糙'
'滇霎蹌櫥啃卯詣踉儼憫邯漳鋸嗔咎芮燁憚筍苯亢璞麓詛猾鸞晦馴葦扼宦揍鯉巳籟'
'趾穢硯汾轍瀚炙辮琛坍窪敝抒竺悚瀕繚蹬訕硝沂嚕濮烯漱犁姍緞揀訥鐸羈霾踝賂'
'烙莆褚峙俐穹茗孚鈣駒婪僥萱瑕倔疹椰鈍靳萃酉哧闕荔釵綏戌墾輒恃曖髏茉毓輾'
'梗熔禎懊璽嬤颶餡砌骷鉀褪郅哽煒瘡嗆錐囉栩噠焱猝癲霹懦祺汲痘墩棣窖唬紊腑'
'靂揖昕蟒瀘鎧羹洱狩玖蝙繽濰璨樺黝阪璀羲晟悸麾檸攙綸踱頷軋梟柿祟殆燉瀆敕'
'檬冢瀝猙韜埠傀饅弼酣葆筠愜葎恙槳咄熠邡嫵憨袂琶瞟雛搐螢酵閆亟忡皙帛檳瘓'
'蠕嘮漣憧蛤髯憬浣骼剌踹跺煜弛誣滌孵稼籬躋榕蹺澗籽琵炕鬢褒吝桀唄稷跤佼狙'
'吮靶筐樟嘰拷屜倭悵脯殉荀蓓惺鄲稠垢孰湃恪奄涇簧甬鏘皖摻咀邃嫡摹痊囤蒿淤'
'宸悴翌愷瑙偎秤噶喵謁淄褻酶儡懵劾荃掣炊餘藹髦暄憔鵲胺峪躥蜒璣怦擄睬惋笠'
'嬪昱鳩颯茸漬攘鍍隘呱曜婕瞰惘衲酪嚓郴絳撾遐抉戍栓騁鉑骯隅迥皋蹊烽巒撮鎬'
'淼疙謐壑矗痰蕙猥樵渲匱暱岱泵驍簌櫚卞胥鴛殯瘩迂呸唧荼歆瘟膺泓胯蜿惦礫咫'
'漉嗒躇煦忑餉矜嗖騾漪闔忐喳蘑悖躊繭伎虯扈縈寐涎俟拴嘈掖搔贅坯啜糯儷呦碾'
'崽瞿蚌飪杞鷺雋忻汐謗鈦釗瓢銬鐲胚薔褥驥臍誨羚琥鏗芋畸篡偕氈鴦滸莘淆掰迢'
'汴芥吆軼撬鷗岷蚩悻禺婧餌簸捺髻頡鸚箋泗坷拗纓圃忒殤冽嗷菠踞岌氟攥貯凋灞'
'幌洙諦蔗壕筏眈癖蝸唰媲葷惰潺掄秧潼踵瀨繕貽殃躡氮逅鄔戾溉粱貂錠疵邂瀛饞'
'砲薈霏薊袒笈瘧臧甥昀纂鵡釉孺釜襖兗逕獒晾筵篝侗俸懺偌惻湄肛喋磐蛾儂茬鎂'
'箍褂罹燎鷲丕誹佯俑斕嵋噥鈉攣翊螂苞夙煲鄴輟鋤燼楣韃蜥痙睽烷藕祐螃猖褶崢'
'曇瘸芊剁婺噎宕苓潞摳鎳熹夯椿簪嫖粑斡蘸嫦摒鬟抨頜礴雹衢畿涪釩唆謨賁娓皚'
'珞涓欒嗇灸癟洵憩聿覃祉蝗叼舷窿蜈婊擢琰偃靨駙訶闌煬羔幔旌吠蒞澇礪耘橢沅'
'啄佇漕溥鈾柚縝馱娩腆沱忱皎恣渥慵甭鞅霽腋楨茱瞠諳潢掂蟾軻軾捎酮弋蟆喆靦'
'誒汞囔滻逵遴睨喏桅錨惴轆渙葩鐺峒潁酯驪娼腓遽祚裱馥榭錮侏槌唏昶颼苻姣痞'
'胰檄濡鯤寮靄膿諺蹋崧黜佰閏泠妊灝粕涮湮蕨枷汩鄱珪饃慫箕蹂噤捋磺斛嬈玥濘'
'紂藺娠貳皰琬躪奐鱸邨罌琨溟杵嶇匝呎罔醺綬潦撅醛慟萼惆祗啷惿晗韭晁帚袞餒'
'淅澹嫗槿緘訛蟄禛糜瞼鉻閭拄贍賒癩犢鉅鉬琌翦詡臆豺郜燮銖蟠佘罄襠閹瘍驤蚣'
'縹謔驃撂蹣俾跚魘緲柑舫詰羯粲舖䡎葙垠稈郢顎跛碉瞌鏤淬咻璟瞑珅妲耆仞珩攫'
'枸嚏湍嶸嚅鉉摁薨囡弒塾驁臼蚤簍蜓鮫焙痣掬珣隼堊牒梆詆饕酗唷鍾杳徨泯蜻暹'
'覬龕粼鄺獷濠啐虢詬挎臾翱盅攆臊傣垛蹴坳羿庾皿秸黠囁哂螳騏幀娣溴唁魷璉頊'
'諂烴譎紈獠鰻娑芍藐祂幗醚覦綰鋰咿嚶恿贇睢燾廄燜骰姝邇渚碘崆鳶擻讒婀誥砥'
'鼾珈鑾闞錳紇夔塹僉縉閡喟笆緹淖鍬佗顥岫咂榔珺嗟盹剽涔譙懋檜瘴玷匍窈裨謾'
'腩黍覲荻愴弁苒玘嚀癬癇詼蝟搪匐旖輦蜃厝淞餮瘀頎宥氤菏嘭啾艮宓遛鰍陂蝨玟'
'喱柩涿摞倌劭豌灤蔻葒噱圩揩盂舀榷邕噔旎隍佃酚窕輜楹佞璜茁箔皈怏獗胴餑胱'
'蚓噯瓚裟亳滎坨剮犒倜漯箴蘚蜴恁酈赧媧綃驊袤僮雉咩櫟槨蠡諄噫挲酰瘠麝嬋邛'
'紜茴爻舐鑣琮脛鏖啻熨靼噙邋殞佚撻嗲蹶齷葏泱篪旻耷瞇顰轂姒喙獼閂擼飭甌孿'
'駟')

LOOKUP_S = {v: k for k, v in enumerate(ALPHABET_S)}
LOOKUP_T = {v: k for k, v in enumerate(ALPHABET_T)}

_BUFFER_1k_e = 1025  # x5
_BUFFER_4k_e = 1023  # x3
_BUFFER_read = 1024


class EncodeError(ValueError):
    pass


class DecodeError(ValueError):
    pass


class SimpleTextWrap():

    def __init__(self, width=35):
        self.width = width
        self.pos = 0

    def write(self, text):
        tlen = len(text)
        pre = self.width - self.pos
        yield text[:pre]
        if tlen < pre:
            self.pos += tlen
            return
        yield '\n'
        if tlen == pre:
            self.pos = 0
            return
        post = tlen - self.width
        if post > pre:
            for i in range(pre, post, self.width):
                yield text[i:i + self.width] + '\n'
            yield text[i + self.width:]
        else:
            yield text[pre:]
            i = pre
        self.pos = (post - i) % self.width
        if not self.pos:
            yield '\n'

    def getvalue(self):
        return self.stream.getvalue()

    @staticmethod
    def wrap(text, width=35):
        ow = SimpleTextWrap(width)
        return ''.join(ow.write(text))


def _iter_stream(stream):
    data = stream.read(_BUFFER_read)
    while data:
        yield from data
        data = stream.read(_BUFFER_read)


def _grouper(iterable, n):
    it = iter(iterable)
    while True:
        chunk = tuple(itertools.islice(it, n))
        if not chunk:
            return
        yield chunk


# xxxxxxxx xx|xxxxxx xxxx|xxxx xxxxxx|xx xxxxxxxx
# 11111111|11 111111|1111 1111|111111 11|11111111
#     0        1         2         3         4

def b1kencode(s, style='s', width=None):
    """Encode the bytes-like object s using Base1k and return a str object.
    style can be 's' or 't' (Simplified/Traditional Chinese).
    if width is an int, wrap the result to this line width.
    """
    if style == 's':
        alphabet = ALPHABET_S
    elif style == 't':
        alphabet = ALPHABET_T
    else:
        raise ValueError('Unknown style')
    # lcm(10, 8) = 5x8
    chk, rem = divmod(len(s), 5)
    # += actually faster
    encoded = ''
    for i in range(chk):
        chunk = s[i * 5:(i + 1) * 5]
        encoded += (
            alphabet[(chunk[0] << 2) | (chunk[1] >> 6)] +
            alphabet[0x3FF & (chunk[1] << 4) | (chunk[2] >> 4)] +
            alphabet[0x3FF & (chunk[2] << 6) | (chunk[3] >> 2)] +
            alphabet[0x3FF & (chunk[3] << 8) | chunk[4]]
        )
    if not rem:
        if width:
            encoded = SimpleTextWrap.wrap(encoded, width)
        return encoded
    chunk = s[chk * 5:]
    if rem == 1:
        encoded += alphabet[chunk[0] << 2]
    elif rem == 2:
        encoded += (
            alphabet[(chunk[0] << 2) | (chunk[1] >> 6)] +
            alphabet[0x3FF & (chunk[1] << 4)]
        )
    elif rem == 3:
        encoded += (
            alphabet[(chunk[0] << 2) | (chunk[1] >> 6)] +
            alphabet[0x3FF & (chunk[1] << 4) | (chunk[2] >> 4)] +
            alphabet[0x3FF & (chunk[2] << 6)]
        )
    elif rem == 4:
        encoded += (
            alphabet[(chunk[0] << 2) | (chunk[1] >> 6)] +
            alphabet[0x3FF & (chunk[1] << 4) | (chunk[2] >> 4)] +
            alphabet[0x3FF & (chunk[2] << 6) | (chunk[3] >> 2)] +
            alphabet[0x3FF & (chunk[3] << 8)]
        )
    encoded += '。'
    if width:
        encoded = SimpleTextWrap.wrap(encoded, width)
    return encoded


def b1kencode_stream(stream, style='s', width=None):
    """Encode the file-like object stream using Base1k and yields one str a time.
    style can be 's' or 't' (Simplified/Traditional Chinese).
    if width is an int, wrap the result to this line width.
    """
    tw = SimpleTextWrap(width)
    data = stream.read(_BUFFER_1k_e)
    while data:
        yield from tw.write(b1kencode(data, style))
        data = stream.read(_BUFFER_1k_e)


def _b1kdecode(it, style='s'):
    if style == 's':
        lookup = LOOKUP_S
    elif style == 't':
        lookup = LOOKUP_T
    else:
        raise ValueError('Unknown style')
    last = None
    undet = None
    state = 0
    for ch in it:
        if ch == '。':
            undet = None
            state = 0
            continue
        num = lookup.get(ch)
        if num is None:
            continue
        elif num > 1023:
            raise DecodeError('Wrong decoder or dictionary. Try b4kdecode.')
        elif state == 0:
            if undet is not None:
                yield undet
                undet = None
            yield num >> 2
            last = num
        elif state == 1:
            yield 0xFF & (last << 6) | (num >> 4)
            last = num
        elif state == 2:
            yield 0xFF & (last << 4) | (num >> 6)
            last = num
        else:
            yield 0xFF & (last << 2) | (num >> 8)
            undet = 0xFF & num
        state = (state + 1) % 4
    if undet is not None:
        yield undet


def b1kdecode(s, style='s'):
    """Decode the Base1k encoded string s.
    The result is returned as a bytes object.
    """
    return bytes(_b1kdecode(s, style))


def b1kdecode_stream(stream, style='s'):
    """Decode the Base1k encoded string s.
    Yields one byte at a time.
    """
    yield from _b1kdecode(_iter_stream(stream), style)


# xxxxxxxx xxxx|xxxx xxxxxxxx
# 11111111|1111 1111|11111111
#     0        1         2

def b4kencode(s, style='s', width=None):
    """Encode the bytes-like object s using Base4k and return a str object.
    style can be 's' or 't' (Simplified/Traditional Chinese).
    if width is an int, wrap the result to this line width.
    """
    if style == 's':
        alphabet = ALPHABET_S
    elif style == 't':
        alphabet = ALPHABET_T
    else:
        raise ValueError('Unknown style')
    # lcm(12, 8) = 3x8
    chk, rem = divmod(len(s), 3)
    # += actually faster
    encoded = ''
    for i in range(chk):
        chunk = s[i * 3:(i + 1) * 3]
        encoded += (
            alphabet[(chunk[0] << 4) | (chunk[1] >> 4)] +
            alphabet[0xFFF & (chunk[1] << 8) | chunk[2]]
        )
    if not rem:
        if width:
            encoded = SimpleTextWrap.wrap(encoded, width)
        return encoded
    chunk = s[chk * 3:]
    if rem == 1:
        encoded += alphabet[chunk[0] << 4]
    elif rem == 2:
        encoded += (
            alphabet[(chunk[0] << 4) | (chunk[1] >> 4)] +
            alphabet[0xFFF & (chunk[1] << 8)]
        )
    encoded += '。'
    if width:
        encoded = SimpleTextWrap.wrap(encoded, width)
    return encoded


def b4kencode_stream(stream, style='s', width=None):
    """Encode the file-like object stream using Base4k and yields one str a time.
    style can be 's' or 't' (Simplified/Traditional Chinese).
    if width is an int, wrap the result to this line width.
    """
    tw = SimpleTextWrap(width)
    data = stream.read(_BUFFER_4k_e)
    while data:
        yield ''.join(tw.write(b4kencode(data, style)))
        data = stream.read(_BUFFER_4k_e)


# xxxxxxxx xxxx|xxxx xxxxxxxx
# 11111111|1111 1111|11111111
#     0        1         2

def _b4kdecode(it, style='s'):
    if style == 's':
        lookup = LOOKUP_S
    elif style == 't':
        lookup = LOOKUP_T
    else:
        raise ValueError('Unknown style')
    last = None
    undet = None
    state = 0
    for ch in it:
        if ch == '。':
            undet = None
            state = 0
            continue
        num = lookup.get(ch)
        if num is None:
            continue
        elif num > 4095:
            raise DecodeError('Wrong decoder or dictionary.')
        elif state:
            yield 0xFF & (last << 4) | (num >> 8)
            undet = 0xFF & num
        else:
            if undet is not None:
                yield undet
                undet = None
            yield num >> 4
            last = num
        state = not state
    if undet is not None:
        yield undet


def b4kdecode(s, style='s'):
    """Decode the Base4k encoded string s.
    The result is returned as a bytes object.
    """
    return bytes(_b4kdecode(s, style))


def b4kdecode_stream(stream, style='s'):
    """Decode the Base4k encoded string s.
    Yields one byte at a time.
    """
    yield from _b4kdecode(_iter_stream(stream), style)


def main(argv):
    b4k = False
    dec = False
    for a in argv:
        if a == '-4k':
            b4k = True
        elif a == '-d':
            dec = True
        else:
            print('Usage: python3 base1k.py [-4k] [-d] < input > output')
            return
    if dec:
        decoder = b4kdecode_stream if b4k else b1kdecode_stream
        for chunk in _grouper(decoder(sys.stdin), 1024):
            sys.stdout.buffer.write(bytes(chunk))
    else:
        encoder = b4kencode_stream if b4k else b1kencode_stream
        for txt in encoder(sys.stdin.buffer, width=35):
            sys.stdout.write(txt)
        sys.stdout.write('\n')

if __name__ == '__main__':
    main(sys.argv[1:])
