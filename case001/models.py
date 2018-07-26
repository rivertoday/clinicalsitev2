# coding:utf-8
from django.db import models

import datetime

# Create your models here.
class ArchivesCases(models.Model):
    GENDER = (
        (u'男', u'男'),
        (u'女', u'女'),
    )
    NATION = (
        (u'汉族', u'汉族'),
        (u'蒙族', u'蒙古族'),
        (u'回族', u'回族'),
        (u'藏族', u'藏族'),
        (u'维吾尔族', u'维吾尔族'),
        (u'苗族', u'苗族'),
        (u'彝族', u'彝族'),
        (u'壮族', u'壮族'),
        (u'布依族', u'布依族'),
        (u'朝鲜族', u'朝鲜族'),
        (u'满族', u'满族'),
        (u'侗族', u'侗族'),
        (u'瑶族', u'瑶族'),
        (u'白族', u'白族'),
        (u'土家族', u'土家族'),
        (u'哈尼族', u'哈尼族'),
        (u'哈萨克族', u'哈萨克族'),
        (u'傣族', u'傣族'),
        (u'黎族', u'黎族'),
        (u'傈傈族', u'傈傈族'),
        (u'佤族', u'佤族'),
        (u'畲族', u'畲族'),
        (u'高山族', u'高山族'),
        (u'拉祜族', u'拉祜族'),
        (u'水族', u'水族'),
        (u'东乡族', u'东乡族'),
        (u'纳西族', u'纳西族'),
        (u'景颇族', u'景颇族'),
        (u'科尔克孜族', u'科尔克孜族'),
        (u'土族', u'土族'),
        (u'达斡尔族', u'达斡尔族'),
        (u'仫佬族', u'仫佬族'),
        (u'羌族', u'羌族'),
        (u'布朗族', u'布朗族'),
        (u'撒拉族', u'撒拉族'),
        (u'毛难族', u'毛难族'),
        (u'仡佬族', u'仡佬族'),
        (u'锡伯族', u'锡伯族'),
        (u'阿昌族', u'阿昌族'),
        (u'普米族', u'普米族'),
        (u'塔吉克族', u'塔吉克族'),
        (u'怒族', u'怒族'),
        (u'乌孜别克族', u'乌孜别克族'),
        (u'俄罗斯族', u'俄罗斯族'),
        (u'鄂温克族', u'鄂温克族'),
        (u'崩龙族', u'崩龙族'),
        (u'保安族', u'保安族'),
        (u'裕固族', u'裕固族'),
        (u'京族', u'京族'),
        (u'塔塔尔族', u'塔塔尔族'),
        (u'独龙族', u'独龙族'),
        (u'鄂伦春族', u'鄂伦春族'),
        (u'赫哲族', u'赫哲族'),
        (u'门巴族', u'门巴族'),
        (u'珞巴族', u'珞巴族'),
        (u'基诺族', u'基诺族'),
        (u'其他', u'其他'),
    )
    AGERNG = (
        (u'20以下', u'<20'),
        (u'20~29', u'20~29'),
        (u'30~39', u'30~39'),
        (u'40以上', u'>=40'),
    )
    MARRIAGE = (
        (u'未婚', u'未婚'),
        (u'已婚', u'已婚'),
        (u'初婚', u'初婚'),
        (u'再婚', u'再婚'),
        (u'复婚', u'复婚'),
        (u'丧偶', u'丧偶'),
        (u'离婚', u'离婚'),
        (u'未说明的婚姻状况', u'未说明的婚姻状况'),
    )
    JOBTYPE = (
        (u'国家机关,党群组织', u'国家机关,党群组织'),
        (u'企业,事业单位', u'企业,事业单位'),
        (u'专业技术人员', u'专业技术人员'),
        (u'家庭主妇', u'家庭主妇'),
        (u'商业,服务业人员', u'商业,服务业人员'),
        (u'农林牧副渔水利业生产人员', u'农林牧副渔水利业生产人员'),
        (u'生产运输设备操作及有关人员', u'生产运输设备操作及有关人员'),
        (u'军人', u'军人'),
        (u'不便分类的其他人员', u'不便分类的其他人员'),
    )
    IDENTYPE = (
        (u'国家公务员', u'国家公务员'),
        (u'专业技术人员', u'专业技术人员'),
        (u'职员', u'职员'),
        (u'企业管理人员', u'企业管理人员'),
        (u'工人', u'工人'),
        (u'农民', u'农民'),
        (u'学生', u'学生'),
        (u'现役军人', u'现役军人'),
        (u'自由职业者', u'自由职业者'),
        (u'个体经营者', u'个体经营者'),
        (u'无业人员', u'无业人员'),
        (u'退(离)休人员', u'退(离)休人员'),
        (u'其他', u'其他'),
    )
    HEIGHTRNG = (
        (u'150cm以下', u'<150'),
        (u'150~159cm', u'150~159'),
        (u'160~169cm', u'160~169'),
        (u'170cm以上', u'>=170'),
    )
    WEIGHTRNG = (
        (u'40kg以下', u'<40'),
        (u'40~49kg', u'40~49'),
        (u'50~59kg', u'50~59'),
        (u'60kg以上', u'>=60'),
    )
    EDULV = (
        (u'小学及以下', u'小学及以下'),
        (u'初中', u'初中'),
        (u'中专/高中', u'中专/高中'),
        (u'大专/大本', u'大专/大本'),
        (u'硕士及以上', u'硕士及以上'),
        (u'其他', u'其他')
    )
    PAYSTYLE = (
        (u'城镇职工基本医疗保险', u'城镇职工基本医疗保险'),
        (u'新城镇居民基本医疗保险', u'新城镇居民基本医疗保险'),
        (u'新型农村合作医疗', u'新型农村合作医疗'),
        (u'贫困救助', u'贫困救助'),
        (u'商业医疗保险', u'商业医疗保险'),
        (u'全公费', u'全公费'),
        (u'全自费', u'全自费'),
        (u'其他社会保险', u'其他社会保险'),
        (u'其他', u'其他'),
    )
    INCOMERNG = (
        (u'500元以下', u'<500'),
        (u'500~1000', u'500~1000'),
        (u'1001~3000', u'1001~3000'),
        (u'3001~5000', u'3001~5000'),
        (u'5001~10000', u'5001~10000'),
        (u'10000以上', u'>10000'),
    )
    TEMPERATURE = (
        (u'小于36℃',u'<36'),
        (u'36.0℃~37.3℃', u'36.0℃~37.3℃'),
        (u'高于37.3℃', u'>37.3℃'),
    )
    PULSE = (
        (u'60-80次/分钟', u'60-80次/分钟'),
        (u'81-100次/分钟', u'81-100次/分钟'),
        (u'100次/分钟以上', u'100次/分钟以上'),
    )
    CASETYPE = (
        (u'社区', u'社区'),
        (u'乡镇', u'乡镇'),
        (u'门诊', u'门诊'),
        (u'住院', u'住院'),
    )
    HTYPE = (
        (u'综合医院', u'综合医院'),
        (u'专科医院', u'专科医院'),
        (u'社区', u'社区'),
        (u'乡镇', u'乡镇'),
    )

    aid = models.BigIntegerField(u'人口学ID')
    acid = models.CharField(u'姓名', max_length=50)
    aSubmitTime = models.DateTimeField(u'建档时间')
    aBirthdate = models.DateField(u'出生日期')
    aSex = models.CharField(u'性别', max_length=1, choices=GENDER, default=u'女')
    acAge = models.CharField(u'年龄段', max_length=8, choices=AGERNG, default=u'30~39')
    aNation = models.CharField(u'民族', max_length=6, choices=NATION, default=u'汉族')
    aMarriage = models.CharField(u'婚姻状况', max_length=16, choices=MARRIAGE, default=u'已婚')
    aJob = models.CharField(u'职业', max_length=50, choices=JOBTYPE, default=u'家庭主妇')
    aIdentity = models.CharField(u'身份', max_length=50, choices=IDENTYPE, default=u'无业人员')
    aHeight = models.CharField(u'身高', max_length=10, choices=HEIGHTRNG, default=u'150~159')
    aWeight = models.CharField(u'体重', max_length=10, choices=WEIGHTRNG, default=u'>=60')
    aEDU = models.CharField(u'教育程度', max_length=10, choices=EDULV, default=u'中专/高中')
    aPayStyle = models.CharField(u'主要医疗付费方式', max_length=50, choices=PAYSTYLE, default=u'新型农村合作医疗')
    aIncome = models.CharField(u'家庭收入', max_length=50, choices=INCOMERNG, default=u'3001~5000')
    aTemperature = models.CharField(u'体温', max_length=20,choices=TEMPERATURE, default=u'36.0℃~37.3℃')
    aPulse = models.CharField(u'脉搏', max_length=20,choices=PULSE, default=u'60-80次/分钟')
    acType = models.CharField(u'病案类别', max_length=6, choices=CASETYPE, default=u'乡镇')
    acHType = models.CharField(u'医院类别', max_length=6, choices=HTYPE, default=u'乡镇')

    def __int__(self):
        return self.acid

class PregnantRecord(models.Model):
    PCOUNT = (
        (u'1次',u'1'),
        (u'2次',u'2'),
        (u'3次',u'3'),
        (u'4次以上',u'>=4'),
    )
    PWAY = (
        (u'顺产',u'顺产'),
        (u'剖腹产',u'剖腹产'),
        (u'其他',u'其他'),
    )
    STARTDAY = (
        (u'0~7天',u'0~7'),
        (u'7~14天',u'7~14'),
        (u'14天以上',u'>14'),
    )
    ILLCOURSE = (
        (u'小于3天',u'<3'),
        (u'3~10天',u'3~10'),
        (u'大于10天',u'>10'),
    )
    RECVEDU = (
        (u'接受过',u'接受过'),
        (u'未接受过',u'未接受过'),
    )
    HISTORY = (
        (u'慢性病史',u'慢性病史'),
        (u'有乳房手术及疾病史',u'有乳房手术及疾病史'),
        (u'服用激素类药物',u'服用激素类药物'),
        (u'家庭其他成员有无类似情况',u'家庭其他成员有无类似情况'),
    )
    people = models.ForeignKey(ArchivesCases, on_delete=models.CASCADE)
    times = models.CharField(u'孕次/产次', max_length=6, choices=PCOUNT, default=u'2')
    birthdate = models.DateField(u'本次孕产日期')
    pregway = models.CharField(u'分娩方式', max_length=10, choices=PWAY, default=u'顺产')
    complication = models.TextField(u'产科并发症', max_length=200)
    malhistory = models.TextField(u'不良妊娠/分娩史', max_length=200)
    malstart = models.CharField(u'起病时间(产后/天)', max_length=10, choices=STARTDAY, default=u'7~14')
    illcourse = models.CharField(u'病程', max_length=10, choices=ILLCOURSE, default=u'3~10')
    recvedu = models.CharField(u'接受母乳宣讲情况', max_length=10, choices=RECVEDU, default=u'未接受过')
    history = models.CharField(u'既往史', max_length=20, choices=HISTORY, default=u'慢性病史')

class LabAnalysis(models.Model):
    people = models.ForeignKey(ArchivesCases, on_delete=models.CASCADE)
    fat = models.FloatField(u'脂肪',max_length=10)
    protein = models.FloatField(u'蛋白质',max_length=10)
    lactose = models.FloatField(u'乳糖',max_length=10)
    total_minerals = models.FloatField(u'总矿物质',max_length=10)

class BreedingInvest(models.Model):
    BMREASON = (
        (u'母乳较健康', u'母乳较健康'),
        (u'增进母子关系', u'增进母子关系'),
        (u'帮助产后身体恢复', u'帮助产后身体恢复'),
        (u'较方便', u'较方便'),
        (u'医院、卫生组织倡导', u'医院、卫生组织倡导'),
        (u'亲友鼓励', u'亲友鼓励'),
        (u'母乳省钱', u'母乳省钱'),
        (u'天经地义的事情', u'天经地义的事情'),
        (u'预防宝宝过敏', u'预防宝宝过敏'),
        (u'其他', u'其他'),
    )
    NBMREASON = (
        (u'没有母乳或母乳量不够，婴儿不够吃', u'没有母乳或母乳量不够，婴儿不够吃'),
        (u'觉得牛奶比较有营养', u'觉得牛奶比较有营养'),
        (u'上下班、外出不方便', u'上下班、外出不方便'),
        (u'婴儿不在身边（如住院、不同住等）', u'婴儿不在身边（如住院、不同住等）'),
        (u'自己生病', u'自己生病'),
        (u'身体不舒服、很累', u'身体不舒服、很累'),
        (u'婴儿拒绝母乳', u'婴儿拒绝母乳'),
        (u'怕胸部变形', u'怕胸部变形'),
        (u'怕疼', u'怕疼'),
        (u'怕孩子以后戒不掉母乳', u'怕孩子以后戒不掉母乳'),
        (u'其他', u'其他'),
    )
    BORING = (
        (u'没有母乳或母乳量不够，婴儿不够吃', u'没有母乳或母乳量不够，婴儿不够吃'),
        (u'觉得牛奶比较有营养',u'觉得牛奶比较有营养'),
        (u'上下班、外出不方便',u'上下班\外出不方便'),
        (u'婴儿不在身边（如住院、不同住等）',u'婴儿不在身边（如住院、不同住等）'),
        (u'自己生病',u'自己生病'),
        (u'身体不舒服、很累',u'身体不舒服、很累'),
        (u'婴儿拒绝母乳',u'婴儿拒绝母乳'),
        (u'怕胸部变形',u'怕胸部变形'),
        (u'怕疼',u'怕疼'),
        (u'怕孩子以后戒不掉母乳',u'怕孩子以后戒不掉母乳'),
        (u'其他',u'其他'),
    )
    CHANNEL = (
        (u'杂志、书籍或育婴手册', u'杂志、书籍或育婴手册'),
        (u'家人、朋友传授', u'家人、朋友传授'),
        (u'孕妇学校', u'孕妇学校'),
        (u'网站、微信、朋友圈、APP', u'网站、微信、朋友圈、APP'),
        (u'没有', u'没有'),
        (u'电视、广播', u'电视、广播'),
        (u'其他', u'其他'),
    )
    HELP_METHOD = (
        (u'自行增加配方奶', u'自行增加配方奶'),
        (u'问有哺乳经验的同龄人', u'问有哺乳经验的同龄人'),
        (u'查询杂志书籍或育儿手册', u'查询杂志书籍或育儿手册'),
        (u'咨询专家医生', u'咨询专家医生'),
        (u'问上一代人，如妈妈或婆婆', u'问上一代人，如妈妈或婆婆'),
        (u'上网查找', u'上网查找'),
        (u'找母乳喂养支持团体', u'找母乳喂养支持团体'),
        (u'拨打生产医院或诊所的哺乳咨询专线', u'拨打生产医院或诊所的哺乳咨询专线'),
        (u'拨打当地哺乳咨询专线', u'拨打当地哺乳咨询专线'),
        (u'其他', u'其他'),
    )
    LACTAGOGUE_KNOWN = (
        (u'催乳食物', u'催乳食物'),
        (u'推拿按摩催乳', u'推拿按摩催乳'),
        (u'中成药', u'中成药'),
        (u'药膳催乳', u'药膳催乳'),
        (u'中药汤剂催乳', u'中药汤剂催乳'),
        (u'针灸催乳', u'针灸催乳'),
        (u'中药熏蒸', u'中药熏蒸'),
        (u'音乐疗法', u'音乐疗法'),
        (u'贴敷', u'贴敷'),
        (u'拔罐催乳', u'拔罐催乳'),
        (u'其他', u'其他'),
    )
    LACTAGOGUE_USED = (
        (u'催乳食物', u'催乳食物'),
        (u'推拿按摩催乳', u'推拿按摩催乳'),
        (u'中成药', u'中成药'),
        (u'药膳催乳', u'药膳催乳'),
        (u'中药汤剂催乳', u'中药汤剂催乳'),
        (u'针灸催乳', u'针灸催乳'),
        (u'中药熏蒸', u'中药熏蒸'),
        (u'音乐疗法', u'音乐疗法'),
        (u'贴敷', u'贴敷'),
        (u'拔罐催乳', u'拔罐催乳'),
        (u'其他', u'其他'),
        (u'没有', u'没有'),
    )
    QUANTYEFFECT = (
        (u'泌乳量增加显著，可满足婴儿需求', u'泌乳量增加显著，可满足婴儿需求'),
        (u'泌乳量稍有增加', u'泌乳量稍有增加'),
        (u'乳汁过多', u'乳汁过多'),
        (u'完全没有改善', u'完全没有改善'),
    )
    BREASTEFFECT = (
        (u'乳房饱满，有胀痛感', u'乳房饱满，有胀痛感'),
        (u'乳房明显充盈，乳汁轻用力挤压即出', u'乳房明显充盈，乳汁轻用力挤压即出'),
        (u'乳房充盈度稍有增加', u'乳房充盈度稍有增加'),
        (u'完全没有改善', u'完全没有改善'),
    )
    MILKEFFECT = (
        (u'完全没有改善', u'完全没有改善'),
        (u'乳汁稀薄改善', u'乳汁稀薄改善'),
        (u'乳汁浓稠改善', u'乳汁浓稠改善'),
    )
    FIRSTTIME = (
        (u'30分钟内', u'30分钟内'),
        (u'30分钟--1个小时', u'30分钟--1个小时'),
        (u'1-2小时', u'1-2小时'),
        (u'2小时以上', u'2小时以上'),
    )
    people = models.ForeignKey(ArchivesCases, on_delete=models.CASCADE)
    breast_reason = models.CharField(u'母乳喂养主要原因', max_length=100, choices=BMREASON)
    not_breast_reason = models.CharField(u'没有母乳喂养的原因', max_length=100, choices=NBMREASON)
    boring_parts = models.CharField(u'母乳喂养最烦恼的部分', max_length=100, choices=BORING)
    channel = models.CharField(u'产前催乳知识学习渠道', max_length=100, choices=CHANNEL)
    help_method = models.CharField(u'乳汁分泌不足会如何处理', max_length=100, choices=HELP_METHOD)
    lactagogue_known = models.CharField(u'知道哪些催乳方式', max_length=100, choices=LACTAGOGUE_KNOWN)
    lactagogue_used = models.CharField(u'曾经采用的催乳方式', max_length=100, choices=LACTAGOGUE_USED)
    quanty_effect = models.CharField(u'采取催乳后泌乳量改善情况', max_length=100, choices=QUANTYEFFECT)
    breast_effect = models.CharField(u'采取催乳后乳房充盈改善情况', max_length=100, choices=BREASTEFFECT)
    milk_effect = models.CharField(u'采取催乳后乳汁质量改善情况', max_length=100, choices=MILKEFFECT)
    first_time = models.CharField(u'产后多久喂母乳', max_length=10, choices=FIRSTTIME)

class TherapyConclusion(models.Model):
    QUANTYEFFECT = (
        (u'完全满足婴儿需要量', u'完全满足婴儿需要量'),
        (u'满足婴儿需要量的2／3', u'满足婴儿需要量的2／3'),
        (u'满足婴儿需要量的1／3', u'满足婴儿需要量的1／3'),
        (u'几乎没有乳汁，不能喂养婴儿', u'几乎没有乳汁，不能喂养婴儿'),
    )
    BREASTEFFECT = (
        (u'乳房饱满，有轻度胀痛感，乳汁自溢', u'乳房饱满，有轻度胀痛感，乳汁自溢'),
        (u'乳房明显充盈，乳汁轻用力挤压即出', u'乳房明显充盈，乳汁轻用力挤压即出'),
        (u'乳房充盈但不胀满，乳汁需用力挤压即出', u'乳房充盈但不胀满，乳汁需用力挤压即出'),
        (u'乳房无明显充盈或胀满感，挤压无乳汁外溢', u'乳房无明显充盈或胀满感，挤压无乳汁外溢'),
    )
    BREASTCHECK1 = (
        (u'无', u'无'),
        (u'有', u'有'),
    )
    BREASTCHECK2 = (
        (u'柔软', u'柔软'),
        (u'胀满', u'胀满'),
        (u'硬结', u'硬结'),
    )
    BREASTCHECK3 = (
        (u'无', u'无'),
        (u'有', u'有'),
    )
    MILKEFFECT = (
        (u'完全没有改善', u'完全没有改善'),
        (u'乳汁稀薄改善', u'乳汁稀薄改善'),
        (u'乳汁浓稠改善', u'乳汁浓稠改善'),
    )
    MILKCHECK1 = (
        (u'白色', u'白色'),
        (u'黄色', u'黄色'),
    )
    MILKCHECK2 = (
        (u'无', u'无'),
        (u'有', u'有'),
    )
    MILKCHECK3 = (
        (u'无', u'无'),
        (u'有', u'有'),
    )
    MILKCHECK4 = (
        (u'无', u'无'),
        (u'有涨奶感，哺乳后仍无缓解', u'有涨奶感，哺乳后仍无缓解'),
        (u'乳房触痛', u'乳房触痛'),
        (u'有泌乳感，但无乳汁排出，乳房持续疼痛', u'有泌乳感，但无乳汁排出，乳房持续疼痛'),
    )
    FIRSTTIME = (
        (u'30分钟内', u'30分钟内'),
        (u'30分钟--1个小时', u'30分钟--1个小时'),
        (u'1-2小时', u'1-2小时'),
        (u'2小时以上', u'2小时以上'),
    )

    FACE = (
        (u'无', u'无'),
        (u'轻度：面色轻微苍白', u'轻度：面色轻微苍白'),
        (u'中度：口唇可见苍白，但未达贫血程度', u'中度：口唇可见苍白，但未达贫血程度'),
        (u'重度：口唇明显苍白，达贫血程度', u'重度：口唇明显苍白，达贫血程度'),
    )
    TIRED = (
        (u'无', u'无'),
        (u'轻度活动即乏力', u'轻度活动即乏力'),
        (u'中度活动感乏力', u'中度活动感乏力'),
        (u'重度活动感乏力', u'重度活动感乏力'),
    )
    HEAD = (
        (u'无', u'无'),
        (u'轻度：偶发头晕，可白行缓解', u'轻度：偶发头晕，可白行缓解'),
        (u'中度：频繁发作，但能坚持工作', u'中度：频繁发作，但能坚持工作'),
        (u'重度：头晕持续不解，影响生活和工作', u'重度：头晕持续不解，影响生活和工作'),
    )
    CHEST = (
        (u'无', u'无'),
        (u'轻度：偶感胸闷，可自行缓解', u'轻度：偶感胸闷，可自行缓解'),
        (u'中度：胸闷发作较频繁，但不影响正常生活和工作', u'中度：胸闷发作较频繁，但不影响正常生活和工作'),
        (u'重度：胸闷持续不解，影响生活和工作', u'重度：胸闷持续不解，影响生活和工作'),
    )
    HEART = (
        (u'无', u'无'),
        (u'轻度：偶感心悸，可自行缓解', u'轻度：偶感心悸，可自行缓解'),
        (u'中度：频繁发作，但能坚持工作', u'中度：频繁发作，但能坚持工作'),
        (u'重度：心悸持续不解，影响生活和工作', u'重度：心悸持续不解，影响生活和工作'),
    )
    MOOD = (
        (u'无', u'无'),
        (u'轻度：小部分时间情志抑郁', u'轻度：小部分时间情志抑郁'),
        (u'中度：相当多时间情志抑郁', u'中度：相当多时间情志抑郁'),
        (u'重度：绝大部分时间或全部时间情志抑郁', u'重度：绝大部分时间或全部时间情志抑郁'),
    )
    SICK = (
        (u'无', u'无'),
        (u'轻度：偶发恶心，可自行缓解', u'轻度：偶发恶心，可自行缓解'),
        (u'中度：频繁发作，但能坚持工作', u'中度：频繁发作，但能坚持工作'),
        (u'重度：恶心持续不解，影响生活和工作', u'重度：恶心持续不解，影响生活和工作'),
    )
    ANOREXIA = (
        (u'无', u'无'),
        (u'轻度：比孕前食量减少量不到1／5', u'轻度：比孕前食量减少量不到1／5'),
        (u'中度：比孕前食量减少l／3～1／4', u'中度：比孕前食量减少l／3～1／4'),
        (u'重度：比孕前食量减少1／2及以上', u'重度：比孕前食量减少1／2及以上'),
    )
    TASTE = (
        (u'无', u'无'),
        (u'轻度：比孕前食量多1／4倍', u'轻度：比孕前食量多1／4倍'),
        (u'中度：比孕前食量多1／2倍', u'中度：比孕前食量多1／2倍'),
        (u'重度：比孕前食量多一倍', u'重度：比孕前食量多一倍'),
    )
    UPD = (
        (u'正常(更换尿布6~8次／300-400ml以上)', u'正常(更换尿布6~8次／300-400ml以上)'),
        (u'过少(更换尿布少于6次／300ml以下)', u'过少(更换尿布少于6次／300ml以下)'),
    )

    TONGUE = (
        (u'舌淡，苔薄白', u'舌淡，苔薄白'),
        (u'舌体正常或暗红，苔淡黄', u'舌体正常或暗红，苔淡黄'),
        (u'舌体正常或微胖，苔薄白', u'舌体正常或微胖，苔薄白'),
        (u'其他', u'其他'),
    )
    PULSECONDITION = (
        (u'脉细', u'脉细'),
        (u'脉弦', u'脉弦'),
        (u'脉滑', u'脉滑'),
         (u'其他', u'其他'),
    )
    PATTERN = (
        (u'肝郁气滞', u'肝郁气滞'),
        (u'痰湿阻滞', u'痰湿阻滞'),
        (u'气血虚弱', u'气血虚弱'),
        (u'其他', u'其他'),
    )
    THERAPY = (
        (u'疏肝解郁，通络下乳', u'疏肝解郁，通络下乳'),
        (u'燥湿祛痰，通经下乳', u'燥湿祛痰，通经下乳'),
        (u'补气养血，佐以通乳', u'补气养血，佐以通乳'),
        (u'其他', u'其他'),
    )
    PRESCRIPTION = (
        (u'下乳涌泉汤', u'下乳涌泉汤'),
        (u'参苓白术散', u'参苓白术散'),
        (u'补中益气汤', u'补中益气汤'),
        (u'其他', u'其他'),
    )

    people = models.ForeignKey(ArchivesCases, on_delete=models.CASCADE)
    # 主证
    quanty_effect = models.CharField(u'采取催乳后泌乳量改善情况', max_length=100, choices=QUANTYEFFECT)
    breast_effect = models.CharField(u'采取催乳后乳房充盈改善情况', max_length=100, choices=BREASTEFFECT)
    breast_check1 = models.CharField(u'乳房检查-乳头凹陷', max_length=10, choices=BREASTCHECK1)
    breast_check2 = models.CharField(u'乳房检查-乳房初诊', max_length=10, choices=BREASTCHECK2)
    breast_check3 = models.CharField(u'乳房检查-压痛', max_length=10, choices=BREASTCHECK3)
    milk_effect = models.CharField(u'采取催乳后乳汁质量改善情况', max_length=100, choices=MILKEFFECT)
    milk_check1 = models.CharField(u'乳汁检查-颜色', max_length=10, choices=MILKCHECK1)
    milk_check2 = models.CharField(u'乳汁检查-清稀', max_length=10, choices=MILKCHECK2)
    milk_check3 = models.CharField(u'乳汁检查-浓稠', max_length=10, choices=MILKCHECK3)
    milk_check4 = models.CharField(u'乳汁检查-淤积', max_length=50, choices=MILKCHECK4)
    first_time = models.CharField(u'产后多久喂母乳', max_length=10, choices=FIRSTTIME)
    # 次证
    face = models.CharField(u'面色少华', max_length=50, choices=FACE)
    tired = models.CharField(u'疲乏无力', max_length=50, choices=TIRED)
    head = models.CharField(u'头晕', max_length=50, choices=HEAD)
    chest = models.CharField(u'胸闷', max_length=50, choices=CHEST)
    heart = models.CharField(u'心悸', max_length=50, choices=HEART)
    mood = models.CharField(u'情志抑郁', max_length=50, choices=MOOD)
    sick = models.CharField(u'恶心', max_length=50, choices=SICK)
    anorexia = models.CharField(u'食欲不振', max_length=50, choices=ANOREXIA)
    taste = models.CharField(u'食多', max_length=50, choices=TASTE)
    upd = models.CharField(u'婴儿每日总尿量', max_length=50, choices=UPD)
    tongue = models.CharField(u'舌体', max_length=50, choices=TONGUE)
    pulse_condition = models.CharField(u'脉象', max_length=50, choices=PULSECONDITION)
    #结论
    pattern = models.CharField(u'中医证型', max_length=50, choices=PATTERN)
    therapy = models.CharField(u'中医治法', max_length=50, choices=THERAPY)
    prescription = models.TextField(u'方药', max_length=50, choices=PRESCRIPTION)
