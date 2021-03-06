# Generated by Django 2.0.6 on 2018-07-26 02:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ArchivesCases',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('aid', models.BigIntegerField(verbose_name='人口学ID')),
                ('acid', models.CharField(max_length=50, verbose_name='姓名')),
                ('aSubmitTime', models.DateTimeField(verbose_name='建档时间')),
                ('aBirthdate', models.DateField(verbose_name='出生日期')),
                ('aSex', models.CharField(choices=[('男', '男'), ('女', '女')], default='女', max_length=1, verbose_name='性别')),
                ('acAge', models.CharField(choices=[('20以下', '<20'), ('20~29', '20~29'), ('30~39', '30~39'), ('40以上', '>=40')], default='30~39', max_length=8, verbose_name='年龄段')),
                ('aNation', models.CharField(choices=[('汉族', '汉族'), ('蒙族', '蒙古族'), ('回族', '回族'), ('藏族', '藏族'), ('维吾尔族', '维吾尔族'), ('苗族', '苗族'), ('彝族', '彝族'), ('壮族', '壮族'), ('布依族', '布依族'), ('朝鲜族', '朝鲜族'), ('满族', '满族'), ('侗族', '侗族'), ('瑶族', '瑶族'), ('白族', '白族'), ('土家族', '土家族'), ('哈尼族', '哈尼族'), ('哈萨克族', '哈萨克族'), ('傣族', '傣族'), ('黎族', '黎族'), ('傈傈族', '傈傈族'), ('佤族', '佤族'), ('畲族', '畲族'), ('高山族', '高山族'), ('拉祜族', '拉祜族'), ('水族', '水族'), ('东乡族', '东乡族'), ('纳西族', '纳西族'), ('景颇族', '景颇族'), ('科尔克孜族', '科尔克孜族'), ('土族', '土族'), ('达斡尔族', '达斡尔族'), ('仫佬族', '仫佬族'), ('羌族', '羌族'), ('布朗族', '布朗族'), ('撒拉族', '撒拉族'), ('毛难族', '毛难族'), ('仡佬族', '仡佬族'), ('锡伯族', '锡伯族'), ('阿昌族', '阿昌族'), ('普米族', '普米族'), ('塔吉克族', '塔吉克族'), ('怒族', '怒族'), ('乌孜别克族', '乌孜别克族'), ('俄罗斯族', '俄罗斯族'), ('鄂温克族', '鄂温克族'), ('崩龙族', '崩龙族'), ('保安族', '保安族'), ('裕固族', '裕固族'), ('京族', '京族'), ('塔塔尔族', '塔塔尔族'), ('独龙族', '独龙族'), ('鄂伦春族', '鄂伦春族'), ('赫哲族', '赫哲族'), ('门巴族', '门巴族'), ('珞巴族', '珞巴族'), ('基诺族', '基诺族'), ('其他', '其他')], default='汉族', max_length=6, verbose_name='民族')),
                ('aMarriage', models.CharField(choices=[('未婚', '未婚'), ('已婚', '已婚'), ('初婚', '初婚'), ('再婚', '再婚'), ('复婚', '复婚'), ('丧偶', '丧偶'), ('离婚', '离婚'), ('未说明的婚姻状况', '未说明的婚姻状况')], default='已婚', max_length=16, verbose_name='婚姻状况')),
                ('aJob', models.CharField(choices=[('国家机关,党群组织', '国家机关,党群组织'), ('企业,事业单位', '企业,事业单位'), ('专业技术人员', '专业技术人员'), ('家庭主妇', '家庭主妇'), ('商业,服务业人员', '商业,服务业人员'), ('农林牧副渔水利业生产人员', '农林牧副渔水利业生产人员'), ('生产运输设备操作及有关人员', '生产运输设备操作及有关人员'), ('军人', '军人'), ('不便分类的其他人员', '不便分类的其他人员')], default='家庭主妇', max_length=50, verbose_name='职业')),
                ('aIdentity', models.CharField(choices=[('国家公务员', '国家公务员'), ('专业技术人员', '专业技术人员'), ('职员', '职员'), ('企业管理人员', '企业管理人员'), ('工人', '工人'), ('农民', '农民'), ('学生', '学生'), ('现役军人', '现役军人'), ('自由职业者', '自由职业者'), ('个体经营者', '个体经营者'), ('无业人员', '无业人员'), ('退(离)休人员', '退(离)休人员'), ('其他', '其他')], default='无业人员', max_length=50, verbose_name='身份')),
                ('aHeight', models.CharField(choices=[('150cm以下', '<150'), ('150~159cm', '150~159'), ('160~169cm', '160~169'), ('170cm以上', '>=170')], default='150~159', max_length=10, verbose_name='身高')),
                ('aWeight', models.CharField(choices=[('40kg以下', '<40'), ('40~49kg', '40~49'), ('50~59kg', '50~59'), ('60kg以上', '>=60')], default='>=60', max_length=10, verbose_name='体重')),
                ('aEDU', models.CharField(choices=[('小学及以下', '小学及以下'), ('初中', '初中'), ('中专/高中', '中专/高中'), ('大专/大本', '大专/大本'), ('硕士及以上', '硕士及以上'), ('其他', '其他')], default='中专/高中', max_length=10, verbose_name='教育程度')),
                ('aPayStyle', models.CharField(choices=[('城镇职工基本医疗保险', '城镇职工基本医疗保险'), ('新城镇居民基本医疗保险', '新城镇居民基本医疗保险'), ('新型农村合作医疗', '新型农村合作医疗'), ('贫困救助', '贫困救助'), ('商业医疗保险', '商业医疗保险'), ('全公费', '全公费'), ('全自费', '全自费'), ('其他社会保险', '其他社会保险'), ('其他', '其他')], default='新型农村合作医疗', max_length=50, verbose_name='主要医疗付费方式')),
                ('aIncome', models.CharField(choices=[('500元以下', '<500'), ('500~1000', '500~1000'), ('1001~3000', '1001~3000'), ('3001~5000', '3001~5000'), ('5001~10000', '5001~10000'), ('10000以上', '>10000')], default='3001~5000', max_length=50, verbose_name='家庭收入')),
                ('aTemperature', models.CharField(choices=[('小于36℃', '<36'), ('36.0℃~37.3℃', '36.0℃~37.3℃'), ('高于37.3℃', '>37.3℃')], default='36.0℃~37.3℃', max_length=20, verbose_name='体温')),
                ('aPulse', models.CharField(choices=[('60-80次/分钟', '60-80次/分钟'), ('81-100次/分钟', '81-100次/分钟'), ('100次/分钟以上', '100次/分钟以上')], default='60-80次/分钟', max_length=20, verbose_name='脉搏')),
                ('acType', models.CharField(choices=[('社区', '社区'), ('乡镇', '乡镇'), ('门诊', '门诊'), ('住院', '住院')], default='乡镇', max_length=6, verbose_name='病案类别')),
                ('acHType', models.CharField(choices=[('综合医院', '综合医院'), ('专科医院', '专科医院'), ('社区', '社区'), ('乡镇', '乡镇')], default='乡镇', max_length=6, verbose_name='医院类别')),
            ],
        ),
        migrations.CreateModel(
            name='BreedingInvest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('breast_reason', models.CharField(choices=[('母乳较健康', '母乳较健康'), ('增进母子关系', '增进母子关系'), ('帮助产后身体恢复', '帮助产后身体恢复'), ('较方便', '较方便'), ('医院、卫生组织倡导', '医院、卫生组织倡导'), ('亲友鼓励', '亲友鼓励'), ('母乳省钱', '母乳省钱'), ('天经地义的事情', '天经地义的事情'), ('预防宝宝过敏', '预防宝宝过敏'), ('其他', '其他')], max_length=100, verbose_name='母乳喂养主要原因')),
                ('not_breast_reason', models.CharField(choices=[('没有母乳或母乳量不够，婴儿不够吃', '没有母乳或母乳量不够，婴儿不够吃'), ('觉得牛奶比较有营养', '觉得牛奶比较有营养'), ('上下班、外出不方便', '上下班、外出不方便'), ('婴儿不在身边（如住院、不同住等）', '婴儿不在身边（如住院、不同住等）'), ('自己生病', '自己生病'), ('身体不舒服、很累', '身体不舒服、很累'), ('婴儿拒绝母乳', '婴儿拒绝母乳'), ('怕胸部变形', '怕胸部变形'), ('怕疼', '怕疼'), ('怕孩子以后戒不掉母乳', '怕孩子以后戒不掉母乳'), ('其他', '其他')], max_length=100, verbose_name='没有母乳喂养的原因')),
                ('boring_parts', models.CharField(choices=[('没有母乳或母乳量不够，婴儿不够吃', '没有母乳或母乳量不够，婴儿不够吃'), ('觉得牛奶比较有营养', '觉得牛奶比较有营养'), ('上下班、外出不方便', '上下班\\外出不方便'), ('婴儿不在身边（如住院、不同住等）', '婴儿不在身边（如住院、不同住等）'), ('自己生病', '自己生病'), ('身体不舒服、很累', '身体不舒服、很累'), ('婴儿拒绝母乳', '婴儿拒绝母乳'), ('怕胸部变形', '怕胸部变形'), ('怕疼', '怕疼'), ('怕孩子以后戒不掉母乳', '怕孩子以后戒不掉母乳'), ('其他', '其他')], max_length=100, verbose_name='母乳喂养最烦恼的部分')),
                ('channel', models.CharField(choices=[('杂志、书籍或育婴手册', '杂志、书籍或育婴手册'), ('家人、朋友传授', '家人、朋友传授'), ('孕妇学校', '孕妇学校'), ('网站、微信、朋友圈、APP', '网站、微信、朋友圈、APP'), ('没有', '没有'), ('电视、广播', '电视、广播'), ('其他', '其他')], max_length=100, verbose_name='产前催乳知识学习渠道')),
                ('help_method', models.CharField(choices=[('自行增加配方奶', '自行增加配方奶'), ('问有哺乳经验的同龄人', '问有哺乳经验的同龄人'), ('查询杂志书籍或育儿手册', '查询杂志书籍或育儿手册'), ('咨询专家医生', '咨询专家医生'), ('问上一代人，如妈妈或婆婆', '问上一代人，如妈妈或婆婆'), ('上网查找', '上网查找'), ('找母乳喂养支持团体', '找母乳喂养支持团体'), ('拨打生产医院或诊所的哺乳咨询专线', '拨打生产医院或诊所的哺乳咨询专线'), ('拨打当地哺乳咨询专线', '拨打当地哺乳咨询专线'), ('其他', '其他')], max_length=100, verbose_name='乳汁分泌不足会如何处理')),
                ('lactagogue_known', models.CharField(choices=[('催乳食物', '催乳食物'), ('推拿按摩催乳', '推拿按摩催乳'), ('中成药', '中成药'), ('药膳催乳', '药膳催乳'), ('中药汤剂催乳', '中药汤剂催乳'), ('针灸催乳', '针灸催乳'), ('中药熏蒸', '中药熏蒸'), ('音乐疗法', '音乐疗法'), ('贴敷', '贴敷'), ('拔罐催乳', '拔罐催乳'), ('其他', '其他')], max_length=100, verbose_name='知道哪些催乳方式')),
                ('lactagogue_used', models.CharField(choices=[('催乳食物', '催乳食物'), ('推拿按摩催乳', '推拿按摩催乳'), ('中成药', '中成药'), ('药膳催乳', '药膳催乳'), ('中药汤剂催乳', '中药汤剂催乳'), ('针灸催乳', '针灸催乳'), ('中药熏蒸', '中药熏蒸'), ('音乐疗法', '音乐疗法'), ('贴敷', '贴敷'), ('拔罐催乳', '拔罐催乳'), ('其他', '其他'), ('没有', '没有')], max_length=100, verbose_name='曾经采用的催乳方式')),
                ('quanty_effect', models.CharField(choices=[('泌乳量增加显著，可满足婴儿需求', '泌乳量增加显著，可满足婴儿需求'), ('泌乳量稍有增加', '泌乳量稍有增加'), ('乳汁过多', '乳汁过多'), ('完全没有改善', '完全没有改善')], max_length=100, verbose_name='采取催乳后泌乳量改善情况')),
                ('breast_effect', models.CharField(choices=[('乳房饱满，有胀痛感', '乳房饱满，有胀痛感'), ('乳房明显充盈，乳汁轻用力挤压即出', '乳房明显充盈，乳汁轻用力挤压即出'), ('乳房充盈度稍有增加', '乳房充盈度稍有增加'), ('完全没有改善', '完全没有改善')], max_length=100, verbose_name='采取催乳后乳房充盈改善情况')),
                ('milk_effect', models.CharField(choices=[('完全没有改善', '完全没有改善'), ('乳汁稀薄改善', '乳汁稀薄改善'), ('乳汁浓稠改善', '乳汁浓稠改善')], max_length=100, verbose_name='采取催乳后乳汁质量改善情况')),
                ('first_time', models.CharField(choices=[('30分钟内', '30分钟内'), ('30分钟--1个小时', '30分钟--1个小时'), ('1-2小时', '1-2小时'), ('2小时以上', '2小时以上')], max_length=10, verbose_name='产后多久喂母乳')),
                ('people', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='case001.ArchivesCases')),
            ],
        ),
        migrations.CreateModel(
            name='LabAnalysis',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fat', models.FloatField(max_length=10, verbose_name='脂肪')),
                ('protein', models.FloatField(max_length=10, verbose_name='蛋白质')),
                ('lactose', models.FloatField(max_length=10, verbose_name='乳糖')),
                ('total_minerals', models.FloatField(max_length=10, verbose_name='总矿物质')),
                ('people', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='case001.ArchivesCases')),
            ],
        ),
        migrations.CreateModel(
            name='PregnantRecord',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('times', models.CharField(choices=[('1次', '1'), ('2次', '2'), ('3次', '3'), ('4次以上', '>=4')], default='2', max_length=6, verbose_name='孕次/产次')),
                ('birthdate', models.DateField(verbose_name='本次孕产日期')),
                ('pregway', models.CharField(choices=[('顺产', '顺产'), ('剖腹产', '剖腹产'), ('其他', '其他')], default='顺产', max_length=10, verbose_name='分娩方式')),
                ('complication', models.TextField(max_length=200, verbose_name='产科并发症')),
                ('malhistory', models.TextField(max_length=200, verbose_name='不良妊娠/分娩史')),
                ('malstart', models.CharField(choices=[('0~7天', '0~7'), ('7~14天', '7~14'), ('14天以上', '>14')], default='7~14', max_length=10, verbose_name='起病时间(产后/天)')),
                ('illcourse', models.CharField(choices=[('小于3天', '<3'), ('3~10天', '3~10'), ('大于10天', '>10')], default='3~10', max_length=10, verbose_name='病程')),
                ('recvedu', models.CharField(choices=[('接受过', '接受过'), ('未接受过', '未接受过')], default='未接受过', max_length=10, verbose_name='接受母乳宣讲情况')),
                ('history', models.CharField(choices=[('慢性病史', '慢性病史'), ('有乳房手术及疾病史', '有乳房手术及疾病史'), ('服用激素类药物', '服用激素类药物'), ('家庭其他成员有无类似情况', '家庭其他成员有无类似情况')], default='慢性病史', max_length=20, verbose_name='既往史')),
                ('people', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='case001.ArchivesCases')),
            ],
        ),
        migrations.CreateModel(
            name='TherapyConclusion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quanty_effect', models.CharField(choices=[('完全满足婴儿需要量', '完全满足婴儿需要量'), ('满足婴儿需要量的2／3', '满足婴儿需要量的2／3'), ('满足婴儿需要量的1／3', '满足婴儿需要量的1／3'), ('几乎没有乳汁，不能喂养婴儿', '几乎没有乳汁，不能喂养婴儿')], max_length=100, verbose_name='采取催乳后泌乳量改善情况')),
                ('breast_effect', models.CharField(choices=[('乳房饱满，有轻度胀痛感，乳汁自溢', '乳房饱满，有轻度胀痛感，乳汁自溢'), ('乳房明显充盈，乳汁轻用力挤压即出', '乳房明显充盈，乳汁轻用力挤压即出'), ('乳房充盈但不胀满，乳汁需用力挤压即出', '乳房充盈但不胀满，乳汁需用力挤压即出'), ('乳房无明显充盈或胀满感，挤压无乳汁外溢', '乳房无明显充盈或胀满感，挤压无乳汁外溢')], max_length=100, verbose_name='采取催乳后乳房充盈改善情况')),
                ('breast_check1', models.CharField(choices=[('无', '无'), ('有', '有')], max_length=10, verbose_name='乳房检查-乳头凹陷')),
                ('breast_check2', models.CharField(choices=[('柔软', '柔软'), ('胀满', '胀满'), ('硬结', '硬结')], max_length=10, verbose_name='乳房检查-乳房初诊')),
                ('breast_check3', models.CharField(choices=[('无', '无'), ('有', '有')], max_length=10, verbose_name='乳房检查-压痛')),
                ('milk_effect', models.CharField(choices=[('完全没有改善', '完全没有改善'), ('乳汁稀薄改善', '乳汁稀薄改善'), ('乳汁浓稠改善', '乳汁浓稠改善')], max_length=100, verbose_name='采取催乳后乳汁质量改善情况')),
                ('milk_check1', models.CharField(choices=[('白色', '白色'), ('黄色', '黄色')], max_length=10, verbose_name='乳汁检查-颜色')),
                ('milk_check2', models.CharField(choices=[('无', '无'), ('有', '有')], max_length=10, verbose_name='乳汁检查-清稀')),
                ('milk_check3', models.CharField(choices=[('无', '无'), ('有', '有')], max_length=10, verbose_name='乳汁检查-浓稠')),
                ('milk_check4', models.CharField(choices=[('无', '无'), ('有涨奶感，哺乳后仍无缓解', '有涨奶感，哺乳后仍无缓解'), ('乳房触痛', '乳房触痛'), ('有泌乳感，但无乳汁排出，乳房持续疼痛', '有泌乳感，但无乳汁排出，乳房持续疼痛')], max_length=50, verbose_name='乳汁检查-淤积')),
                ('first_time', models.CharField(choices=[('30分钟内', '30分钟内'), ('30分钟--1个小时', '30分钟--1个小时'), ('1-2小时', '1-2小时'), ('2小时以上', '2小时以上')], max_length=10, verbose_name='产后多久喂母乳')),
                ('face', models.CharField(choices=[('无', '无'), ('轻度：面色轻微苍白', '轻度：面色轻微苍白'), ('中度：口唇可见苍白，但未达贫血程度', '中度：口唇可见苍白，但未达贫血程度'), ('重度：口唇明显苍白，达贫血程度', '重度：口唇明显苍白，达贫血程度')], max_length=50, verbose_name='面色少华')),
                ('tired', models.CharField(choices=[('无', '无'), ('轻度活动即乏力', '轻度活动即乏力'), ('中度活动感乏力', '中度活动感乏力'), ('重度活动感乏力', '重度活动感乏力')], max_length=50, verbose_name='疲乏无力')),
                ('head', models.CharField(choices=[('无', '无'), ('轻度：偶发头晕，可白行缓解', '轻度：偶发头晕，可白行缓解'), ('中度：频繁发作，但能坚持工作', '中度：频繁发作，但能坚持工作'), ('重度：头晕持续不解，影响生活和工作', '重度：头晕持续不解，影响生活和工作')], max_length=50, verbose_name='头晕')),
                ('chest', models.CharField(choices=[('无', '无'), ('轻度：偶感胸闷，可自行缓解', '轻度：偶感胸闷，可自行缓解'), ('中度：胸闷发作较频繁，但不影响正常生活和工作', '中度：胸闷发作较频繁，但不影响正常生活和工作'), ('重度：胸闷持续不解，影响生活和工作', '重度：胸闷持续不解，影响生活和工作')], max_length=50, verbose_name='胸闷')),
                ('heart', models.CharField(choices=[('无', '无'), ('轻度：偶感心悸，可自行缓解', '轻度：偶感心悸，可自行缓解'), ('中度：频繁发作，但能坚持工作', '中度：频繁发作，但能坚持工作'), ('重度：心悸持续不解，影响生活和工作', '重度：心悸持续不解，影响生活和工作')], max_length=50, verbose_name='心悸')),
                ('mood', models.CharField(choices=[('无', '无'), ('轻度：小部分时间情志抑郁', '轻度：小部分时间情志抑郁'), ('中度：相当多时间情志抑郁', '中度：相当多时间情志抑郁'), ('重度：绝大部分时间或全部时间情志抑郁', '重度：绝大部分时间或全部时间情志抑郁')], max_length=50, verbose_name='情志抑郁')),
                ('sick', models.CharField(choices=[('无', '无'), ('轻度：偶发恶心，可自行缓解', '轻度：偶发恶心，可自行缓解'), ('中度：频繁发作，但能坚持工作', '中度：频繁发作，但能坚持工作'), ('重度：恶心持续不解，影响生活和工作', '重度：恶心持续不解，影响生活和工作')], max_length=50, verbose_name='恶心')),
                ('anorexia', models.CharField(choices=[('无', '无'), ('轻度：比孕前食量减少量不到1／5', '轻度：比孕前食量减少量不到1／5'), ('中度：比孕前食量减少l／3～1／4', '中度：比孕前食量减少l／3～1／4'), ('重度：比孕前食量减少1／2及以上', '重度：比孕前食量减少1／2及以上')], max_length=50, verbose_name='食欲不振')),
                ('taste', models.CharField(choices=[('无', '无'), ('轻度：比孕前食量多1／4倍', '轻度：比孕前食量多1／4倍'), ('中度：比孕前食量多1／2倍', '中度：比孕前食量多1／2倍'), ('重度：比孕前食量多一倍', '重度：比孕前食量多一倍')], max_length=50, verbose_name='食多')),
                ('upd', models.CharField(choices=[('正常(更换尿布6~8次／300-400ml以上)', '正常(更换尿布6~8次／300-400ml以上)'), ('过少(更换尿布少于6次／300ml以下)', '过少(更换尿布少于6次／300ml以下)')], max_length=50, verbose_name='婴儿每日总尿量')),
                ('tongue', models.CharField(choices=[('舌淡，苔薄白', '舌淡，苔薄白'), ('舌体正常或暗红，苔淡黄', '舌体正常或暗红，苔淡黄'), ('舌体正常或微胖，苔薄白', '舌体正常或微胖，苔薄白'), ('其他', '其他')], max_length=50, verbose_name='舌体')),
                ('pulse_condition', models.CharField(choices=[('脉细', '脉细'), ('脉弦', '脉弦'), ('脉滑', '脉滑'), ('其他', '其他')], max_length=50, verbose_name='脉象')),
                ('pattern', models.CharField(choices=[('肝郁气滞', '肝郁气滞'), ('痰湿阻滞', '痰湿阻滞'), ('气血虚弱', '气血虚弱'), ('其他', '其他')], max_length=50, verbose_name='中医证型')),
                ('therapy', models.CharField(choices=[('疏肝解郁，通络下乳', '疏肝解郁，通络下乳'), ('燥湿祛痰，通经下乳', '燥湿祛痰，通经下乳'), ('补气养血，佐以通乳', '补气养血，佐以通乳'), ('其他', '其他')], max_length=50, verbose_name='中医治法')),
                ('prescription', models.TextField(choices=[('下乳涌泉汤', '下乳涌泉汤'), ('参苓白术散', '参苓白术散'), ('补中益气汤', '补中益气汤'), ('其他', '其他')], max_length=50, verbose_name='方药')),
                ('people', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='case001.ArchivesCases')),
            ],
        ),
    ]
