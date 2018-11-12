# -*- coding: utf-8 -*-
from django.db import models

# Create your models here.

#一、一般情况
class GeneralInfo(models.Model):
    TITLE = (
        (u'主任医师', u'主任医师'),
        (u'副主任医师', u'副主任医师'),
        (u'主治医师', u'主治医师'),
    )
    BLOOD_TYPE = (
        (u'A', u'A'),
        (u'B', u'B'),
        (u'O', u'O'),
        (u'AB', u'AB'),
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
    CAREER = (
        (u'学生', u'学生'),
        (u'个体', u'个体'),
        (u'农民', u'农民'),
        (u'军人', u'军人'),
        (u'工人', u'工人'),
        (u'财会人员', u'财会人员'),
        (u'技术人员', u'技术人员'),
        (u'服务业', u'服务业'),
        (u'科教文卫', u'科教文卫'),
        (u'行政管理', u'行政管理'),
        (u'无业', u'无业'),
        (u'其它', u'其它'),
    )
    ENTRANCE = (
        (u'门诊', u'门诊'),
        (u'病房', u'病房'),
    )
    CULTURE = (
        (u'文盲', u'文盲'),
        (u'小学及以下', u'小学及以下'),
        (u'中学或中专', u'中学或中专'),
        (u'大专', u'大专'),
        (u'本科', u'本科'),
        (u'研究生及以上', u'研究生及以上'),
    )
    MARRIAGE = (
        (u'未婚无性生活', u'未婚无性生活'),
        (u'未婚有性生活', u'未婚有性生活'),
        (u'已婚同居', u'已婚同居'),
        (u'已婚分居', u'已婚分居'),
        (u'离婚', u'离婚'),
    )

    recdate = models.DateField(verbose_name=u'日期', blank=True,default=date.today)
    serial = models.CharField(verbose_name=u'问卷编码',max_length=50)
    hospital = models.CharField(verbose_name=u'医院名称',max_length=100)
    expert = models.CharField(verbose_name=u'填表专家姓名',max_length=50)
    title = models.CharField(verbose_name=u'职称',choices=TITLE, max_length=30)
    name = models.CharField(verbose_name=u'患者姓名', max_length=50)
    telephone = models.CharField(verbose_name=u'电话', max_length=20)
    age = models.IntegerField(verbose_name=u'年龄')
    height = models.IntegerField(verbose_name=u'身高cm')
    weight = models.DecimalField(verbose_name=u'体重kg',max_digits=4,decimal_places=1)
    blood_type = models.CharField(verbose_name=u'血型',choices=BLOOD_TYPE, max_length=10)
    nation = models.CharField(verbose_name=u'民族',choices=NATION, max_length=20)
    career = models.CharField(verbose_name=u'职业',choices=CAREER, max_length=20)
    #spec_env = models.ForeignKey(GeneralSpecEnv, on_delete=models.CASCADE)
    address = models.CharField(verbose_name=u'病人现住址',max_length=100)
    entrance = models.CharField(verbose_name=u'病人来源',choices=ENTRANCE, max_length=10)
    culture = models.CharField(verbose_name=u'文化程度',choices=CULTURE, max_length=30)
    marriage = models.CharField(verbose_name=u'婚姻状况',choices=MARRIAGE, max_length=30)
    #eat_hobbies = models.ForeignKey(GeneralEatHobbies, on_delete=models.CASCADE)

    def __int__(self):
        return self.name

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = u'一般情况'

#一般情况-特殊工作环境
class GeneralSpecEnv(models.Model):
    gaokong = models.BooleanField(verbose_name=u'高空')
    diwen = models.BooleanField(verbose_name=u'低温')
    zaosheng = models.BooleanField(verbose_name=u'噪声')
    fushe = models.BooleanField(verbose_name=u'辐射')
    huagongwuran = models.BooleanField(verbose_name=u'化工污染')
    julieyundong = models.BooleanField(verbose_name=u'剧烈运动')
    qiyou = models.BooleanField(verbose_name=u'汽油')
    wu = models.BooleanField(verbose_name=u'无')

    person = models.OneToOneField(GeneralInfo, on_delete=models.CASCADE)

    class Meta:
        verbose_name = u'特殊工作环境'

#一般情况-饮食偏好
class GeneralEatHobbies(models.Model):
    wuteshu = models.BooleanField(verbose_name=u'无特殊')
    sushi = models.BooleanField(verbose_name=u'素食')
    suan = models.BooleanField(verbose_name=u'酸')
    tian = models.BooleanField(verbose_name=u'甜')
    xian = models.BooleanField(verbose_name=u'咸')
    xinla = models.BooleanField(verbose_name=u'辛辣')
    you = models.BooleanField(verbose_name=u'油')
    shengleng = models.BooleanField(verbose_name=u'生冷')
    kafei = models.BooleanField(verbose_name=u'含咖啡因食物或饮品')
    qita = models.BooleanField(verbose_name=u'其它')
    qita_desc = models.CharField(verbose_name=u'其它说明', max_length=50, default=u'无')

    person = models.OneToOneField(GeneralInfo, on_delete=models.CASCADE)

    class Meta:
        verbose_name = u'饮食偏好'

################################################################################
#二、月经情况
class Menstruation(models.Model):
    CYCLICITY = (
        (u'尚规律', u'尚规律'),
        (u'不规律', u'不规律'),
    )
    ABNORMAL = (
        (u'或提前7天以上', u'或提前7天以上'),
        (u'或1月多次', u'或1月多次'),
        (u'或数月1次', u'或数月1次'),
    )
    CYCLICITY_SUM = (
        (u'不足2天', u'不足2天'),
        (u'3-7天', u'3-7天'),
        (u'7天以上', u'7天以上'),
        (u'有时几日即净，有时7日以上甚至达半月余不净', u'有时几日即净，有时7日以上甚至达半月余不净'),
    )
    BLOOD_COND = (
        (u'出血量中等，每次约需5-20张卫生巾', u'出血量中等，每次约需5-20张卫生巾'),
        (u'出血量多，每次多于20张卫生巾', u'出血量多，每次多于20张卫生巾'),
        (u'经量少，每次少于5张卫生巾', u'经量少，每次少于5张卫生巾'),
        (u'经量极少，几乎不用卫生巾，用护垫即可', u'经量极少，几乎不用卫生巾，用护垫即可'),
    )
    BLOOD_COLOR = (
        (u'淡红', u'淡红'),
        (u'鲜红', u'鲜红'),
        (u'暗红', u'暗红'),
        (u'紫红', u'紫红'),
        (u'紫黯', u'紫黯'),
        (u'紫黑', u'紫黑'),
        (u'褐色', u'褐色'),
        (u'其他', u'其他'),
    )
    BLOOD_QUALITY = (
        (u'正常', u'正常'),
        (u'粘稠', u'粘稠'),
        (u'清稀', u'清稀'),
    )
    BLOOD_BLOCK = (
        (u'无', u'无'),
        (u'偶有', u'偶有'),
        (u'常夹少量小血块', u'常夹少量小血块'),
        (u'常夹较大血块', u'常夹较大血块'),
    )
    BLOOD_CHARACTER = (
        (u'顺畅', u'顺畅'),
        (u'势急暴下', u'势急暴下'),
        (u'淋漓不断', u'淋漓不断'),
        (u'点滴即净', u'点滴即净'),
    )

    person = models.OneToOneField(GeneralInfo, on_delete=models.CASCADE)
    first_time = models.IntegerField(verbose_name=u'初潮年龄')
    cyclicity = models.CharField(verbose_name=u'月经周期',choices=CYCLICITY, max_length=20)
    normal = models.IntegerField(verbose_name=u'月经规律间隔天数', blank=True, null=True)
    abnormal = models.CharField(verbose_name=u'月经不规律', choices=ABNORMAL, max_length=30, blank=True, null=True)
    cyclicity_sum = models.CharField(verbose_name=u'行经天数', choices=CYCLICITY_SUM, max_length=100)
    blood_amount = models.IntegerField(verbose_name=u'出血量所需卫生巾数')
    blood_cond = models.CharField(verbose_name=u'出血情况', choices=BLOOD_COND, max_length=100)
    blood_color = models.CharField(verbose_name=u'出血颜色', choices=BLOOD_COLOR, max_length=10)
    blood_quality = models.CharField(verbose_name=u'出血质地', choices=BLOOD_QUALITY, max_length=10)
    blood_block = models.CharField(verbose_name=u'血块', choices=BLOOD_BLOCK, max_length=30)
    blood_character = models.CharField(verbose_name=u'出血特点', choices=BLOOD_CHARACTER, max_length=20)

    class Meta:
        verbose_name = u'月经情况'

################################################################################
#三、全身症状
class Symptom(models.Model):
    person = models.OneToOneField(GeneralInfo, on_delete=models.CASCADE)
    serial = models.IntegerField(verbose_name=u'全身症状对应患者编号', default=-1)
    #spirit = models.ForeignKey(SymptomSpirit, on_delete=models.CASCADE)
    #mood = models.ForeignKey(SymptomMood, on_delete=models.CASCADE)
    #chill_fever = models.ForeignKey(SymptomChillFever, on_delete=models.CASCADE)

    class Meta:
        verbose_name = u'全身症状'

#三、全身症状-精神
class SymptomSpirit(models.Model):
    jinglichongpei = models.BooleanField(verbose_name=u'精力充沛')
    jianwang = models.BooleanField(verbose_name=u'健忘')
    jingshenbujizhong = models.BooleanField(verbose_name=u'精神不集中')
    shenpifali = models.BooleanField(verbose_name=u'神疲乏力')
    yalida = models.BooleanField(verbose_name=u'学习、工作压力大')
    jiaodabiangu = models.BooleanField(verbose_name=u'个人/家庭遭遇较大变故')
    beishangyuku = models.BooleanField(verbose_name=u'悲伤欲哭')

    symptom = models.OneToOneField(Symptom, on_delete=models.CASCADE)

    class Meta:
        verbose_name = u'精神状况'

#全身症状-情绪
class SymptomMood(models.Model):
    zhengchang = models.BooleanField(verbose_name=u'正常')
    leguankailang = models.BooleanField(verbose_name=u'乐观开朗')
    silvguodu = models.BooleanField(verbose_name=u'思虑过度')
    xinuwuchang = models.BooleanField(verbose_name=u'喜怒无常')
    fanzaoyinu = models.BooleanField(verbose_name=u'烦躁易怒')
    jiaolv = models.BooleanField(verbose_name=u'焦虑')
    beishangyuku = models.BooleanField(verbose_name=u'悲伤欲哭')
    yiyu = models.BooleanField(verbose_name=u'抑郁')
    duosiduolv = models.BooleanField(verbose_name=u'多思多虑')
    qita = models.BooleanField(verbose_name=u'其它')
    qita_desc = models.CharField(verbose_name=u'其它说明', max_length=100, default=u'无')

    symptom = models.OneToOneField(Symptom, on_delete=models.CASCADE)

    class Meta:
        verbose_name = u'情绪状况'

#全身症状-寒热
class SymptomChillFever(models.Model):
    zhengchang = models.BooleanField(verbose_name=u'正常')
    weihan = models.BooleanField(verbose_name=u'畏寒')
    wuxinfanre = models.BooleanField(verbose_name=u'五心烦热')
    wuhouchaore = models.BooleanField(verbose_name=u'午后潮热')
    direbutui = models.BooleanField(verbose_name=u'低热不退')

    symptom = models.OneToOneField(Symptom, on_delete=models.CASCADE)

    class Meta:
        verbose_name = u'寒热状况'

#全身症状-头
class SymptomHead(models.Model):
    zhengchang = models.BooleanField(verbose_name=u'正常')
    touyun = models.BooleanField(verbose_name=u'头晕')
    toutong = models.BooleanField(verbose_name=u'头痛')
    touchenzhong = models.BooleanField(verbose_name=u'头沉重')

    symptom = models.OneToOneField(Symptom, on_delete=models.CASCADE)

    class meta:
        verbose_name = u'头部状况'


#全身症状-目
class SymptomEyes(models.Model):
    zhengchang = models.BooleanField(verbose_name=u'正常')
    muxuan = models.BooleanField(verbose_name=u'目眩')
    muse = models.BooleanField(verbose_name=u'目涩')
    yanhua = models.BooleanField(verbose_name=u'眼花')
    mutong = models.BooleanField(verbose_name=u'目痛')
    muyang = models.BooleanField(verbose_name=u'目痒')
    chenqifz = models.BooleanField(verbose_name=u'晨起眼睑浮肿')

    symptom = models.OneToOneField(Symptom, on_delete=models.CASCADE)

    class meta:
        verbose_name = u'眼部状况'

#全身症状-耳
class SymptomEar(models.modle):
    erming = models.BooleanField(verbose_name=u'耳鸣')
    erlong = models.BooleanField(verbose_name=u'耳聋')
    tinglibq = models.BooleanField(verbose_name=u'听力不清，声音重复')

    symptom = models.OneToOneField(Symptom, on_delete=models.CASCADE)

    class meta:
        verbose_name = u'听力状况'


#全身症状-咽喉
class SymptomThroat(models.modle):
    zhengchang = models.BooleanField(verbose_name=u'正常')
    yangan = models.BooleanField(verbose_name=u'咽干')
    yantong = models.BooleanField(verbose_name=u'咽痛')
    yanyang = models.BooleanField(verbose_name=u'咽痒')
    yiwugan = models.BooleanField(verbose_name=u'异物感')

    symptom = models.OneToOneField(Symptom, on_delete=models.CASCADE)

    class meta:
        verbose_name = u'咽喉状况'

#全身症状-口味
class SymptomBreath(models.modle):
    wuyiwei = models.BooleanField(verbose_name=u'口中无异味')
    kouku = models.BooleanField(verbose_name=u'口苦')
    kougan = models.BooleanField(verbose_name=u'口干')
    koudan = models.BooleanField(verbose_name=u'口淡')
    kouxian = models.BooleanField(verbose_name=u'口咸')
    koutian = models.BooleanField(verbose_name=u'口甜')
    kounian = models.BooleanField(verbose_name=u'口粘')
    danyuss= models.BooleanField(verbose_name=u'但欲漱水不欲咽')

    symptom = models.OneToOneField(Symptom, on_delete=models.CASCADE)

    class meta:
        verbose_name = u'口味状况'


#全身症状-饮食
class SymptomDiet(models.modle):
    nadaishishao = models.BooleanField(verbose_name=u'纳呆食少')
    shiyuws = models.BooleanField(verbose_name=u'食欲旺盛，多食易饥')
    yanshi = models.BooleanField(verbose_name=u'厌食')
    xireyin = models.BooleanField(verbose_name=u'喜热饮')
    xilengyin = models.BooleanField(verbose_name=u'喜冷饮')
    shiyujiantui = models.BooleanField(verbose_name=u'食欲减退，食少')
    shihoufuzhang = models.BooleanField(verbose_name=u'食后腹胀')
    shixinla = models.BooleanField(verbose_name=u'喜辛辣')
    shishengleng = models.BooleanField(verbose_name=u'喜生冷')
    kebuduoyin = models.BooleanField(verbose_name=u'渴不多饮')


    symptom = models.OneToOneField(Symptom, on_delete=models.CASCADE)


    class meta:
        verbose_name = u'饮食状况'

#全身症状-睡眠
class SymptomSleep(models.modle):
    zhengchang = models.BooleanField(verbose_name=u'正常')
    yiban = models.BooleanField(verbose_name=u'一般')
    duomengyixing = models.BooleanField(verbose_name=u'多梦易醒')
    nanyirumian = models.BooleanField(verbose_name=u'难以入眠')
    cheyebumian = models.BooleanField(verbose_name=u'彻夜不眠')
    duomeng = models.BooleanField(verbose_name=u'多梦')
    shishui = models.BooleanField(verbose_name=u'嗜睡')

    symptom = models.OneToOneField(Symptom, on_delete=models.CASCADE)

    class meta:
        verbose_name = u'睡眠状况'

#全身症状-大便
class SymptomStool(models.modle):
    sehuang = models.BooleanField(verbose_name=u'色黄，通畅，成形不干燥')
    bianmi = models.BooleanField(verbose_name=u'便秘')
    zhixi = models.BooleanField(verbose_name=u'质稀')
    sgsx = models.BooleanField(verbose_name=u'时干时稀')
    xiexie = models.BooleanField(verbose_name=u'泄泻')
    tlzqxiexie = models.BooleanField(verbose_name=u'天亮前泄泻')
    zhinian = models.BooleanField(verbose_name=u'质黏，有排不尽之感')
    weixiaohua = models.BooleanField(verbose_name=u'大便中夹有未消化食物')


    symptom = models.OneToOneField(Symptom, on_delete=models.CASCADE)


    class meta:
        verbose_name = u'大便状况'


#全身症状-小便
class SymptomUrine(models.modle):
    zhengchang = models.BooleanField(verbose_name=u'正常')
    duanchi = models.BooleanField(verbose_name=u'短赤')
    duanhuang = models.BooleanField(verbose_name=u'短黄')
    qingchang = models.BooleanField(verbose_name=u'清长')
    yeniaopin = models.BooleanField(verbose_name=u'夜尿频')
    xbpinshu= models.BooleanField(verbose_name=u'小便频数')
    niaoji= models.BooleanField(verbose_name=u'尿急')
    niaotong= models.BooleanField(verbose_name=u'尿痛')
    shaoniao= models.BooleanField(verbose_name=u'少尿')
    yulibujin= models.BooleanField(verbose_name=u'余沥不尽')

    symptom = models.OneToOneField(Symptom, on_delete=models.CASCADE)


    class meta:
        verbose_name = u'小便状况'

#全身症状-四肢
class SymptomLimb(models.modle):
    zhengchang = models.BooleanField(verbose_name=u'正常')
    wuli = models.BooleanField(verbose_name=u'无力')
    mamu = models.BooleanField(verbose_name=u'麻木')
    kunzhong = models.BooleanField(verbose_name=u'困重')
    zhileng = models.BooleanField(verbose_name=u'肢冷')
    bingliang = models.BooleanField(verbose_name=u'冰凉')
    szxinre = models.BooleanField(verbose_name=u'手足心热')
    fuzhong = models.BooleanField(verbose_name=u'浮肿')

    symptom = models.OneToOneField(Symptom, on_delete=models.CASCADE)


    class meta:
        verbose_name = u'四肢状况'

#全身症状-其他
class SymptomOther(models.modle):
    wu = models.BooleanField(verbose_name=u'无')
    czjdanbai = models.BooleanField(verbose_name=u'唇爪甲淡白')
    xyjiantui = models.BooleanField(verbose_name=u'性欲减退')

    symptom = models.OneToOneField(Symptom, on_delete=models.CASCADE)

    class meta:
        verbose_name = u'其他状况'

#全身症状-舌质
class SymptomTtexture(models.modle):
    danhong = models.BooleanField(verbose_name=u'淡红')
    danbai = models.BooleanField(verbose_name=u'淡白')
    pianhong = models.BooleanField(verbose_name=u'偏红')
    danan = models.BooleanField(verbose_name=u'淡黯')
    zian = models.BooleanField(verbose_name=u'紫黯')
    yudian = models.BooleanField(verbose_name=u'有瘀点或瘀斑')

    symptom = models.OneToOneField(Symptom, on_delete=models.CASCADE)

    class meta:
        verbose_name = u'舌质状况'

#全身症状-舌苔
class SymptomCoating(models.modle):
    bai = models.BooleanField(verbose_name=u'白')
    huang = models.BooleanField(verbose_name=u'黄')
    ni = models.BooleanField(verbose_name=u'腻')
    bo = models.BooleanField(verbose_name=u'薄')
    hou = models.BooleanField(verbose_name=u'厚')
    run = models.BooleanField(verbose_name=u'润')
    hua = models.BooleanField(verbose_name=u'滑')
    hhouni = models.BooleanField(verbose_name=u'黄厚腻')
    bairun = models.BooleanField(verbose_name=u'白润')
    huangcao = models.BooleanField(verbose_name=u'黄糙')
    wutai = models.BooleanField(verbose_name=u'无苔')
    shaotai = models.BooleanField(verbose_name=u'少苔')
    huabo = models.BooleanField(verbose_name=u'花剥')

    symptom = models.OneToOneField(Symptom, on_delete=models.CASCADE)

    class meta:
        verbose_name = u'舌苔状况'

# 全身症状-舌体
class SymptomTongue(models.modle):
    shoubo = models.BooleanField(verbose_name=u'瘦薄')
    pangda = models.BooleanField(verbose_name=u'胖大')
    bianjianhong = models.BooleanField(verbose_name=u'边尖红')
    youchihen = models.BooleanField(verbose_name=u'有齿痕')
    zhongyouliewen = models.BooleanField(verbose_name=u'中有裂纹')

    symptom = models.OneToOneField(Symptom, on_delete=models.CASCADE)

    class meta:
        verbose_name = u'舌体状况'

#全身症状-脉象
class SymptomPulse(models.modle):
    shi = models.BooleanField(verbose_name=u'实')
    fu = models.BooleanField(verbose_name=u'浮')
    chen = models.BooleanField(verbose_name=u'沉')
    chi = models.BooleanField(verbose_name=u'迟')
    huan = models.BooleanField(verbose_name=u'缓')
    xi = models.BooleanField(verbose_name=u'细')
    ruo = models.BooleanField(verbose_name=u'弱')
    shu = models.BooleanField(verbose_name=u'数')
    hua = models.BooleanField(verbose_name=u'滑')
    se = models.BooleanField(verbose_name=u'涩')
    xian = models.BooleanField(verbose_name=u'弦')
    jin = models.BooleanField(verbose_name=u'紧')
    kou = models.BooleanField(verbose_name=u'芤')
    ru = models.BooleanField(verbose_name=u'濡')
    hong = models.BooleanField(verbose_name=u'洪')
    youli = models.BooleanField(verbose_name=u'有力')
    wuli = models.BooleanField(verbose_name=u'无力')

    symptom = models.OneToOneField(Symptom, on_delete=models.CASCADE)

    class meta:
        verbose_name = u'脉象'

################################################################################
#四、其它
class Other(models.Model):
    BORNCOND = (
        (u'早产（28周-37周）', u'早产（28周-37周）'),
        (u'足月产', u'足月产'),
        (u'阴道分娩', u'阴道分娩'),
        (u'剖宫产', u'剖宫产'),
    )
    BODYCOND = (
        (u'好',u'好'),
        (u'一般', u'一般'),
        (u'易疲劳乏力', u'易疲劳乏力'),
    )
    CAREERLABOR = (
        (u'重体力劳动（如：搬运工、清洁工、农场工人、畜牧场工人等）',u'重体力劳动（如：搬运工、清洁工、农场工人、畜牧场工人等）'),
        (u'中体力劳动（如：家政服务人员、服务生、厨师、护士等）', u'中体力劳动（如：家政服务人员、服务生、厨师、护士等）'),
        (u'轻体力劳动（如：教师、美容美发师、批发商、职员等）', u'中体力劳动（如：教师、美容美发师、批发商、职员等）'),
        (u'坐式的工作（如：收银员、出纳员、接线员、秘书等）', u'坐式的工作（如：收银员、出纳员、接线员、秘书等）'),
    )
    POORBLOOD = (
        (u'不详',u'不详'),
        (u'贫血', u'贫血'),
        (u'不贫血', u'不贫血'),
    )
    PHYCIALEXER = (
        (u'无',u'无'),
        (u'很少（≤1次/周）', u'很少（≤1次/周）'),
        (u'偶尔（≤3次/周）', u'偶尔（≤3次/周）'),
        (u'经常（≥4次/周）', u'经常（≥4次/周）'),
        (u'一般（少量出汗，心率≤120次/分）', u'一般（少量出汗，心率≤120次/分）'),
        (u'高强度（大汗淋漓，心率>120次/分）', u'高强度（大汗淋漓，心率>120次/分）'),
    )
    #一级亲属（母亲、姐妹、女儿）异常子宫出血史
    WOMBBLOOD = (
        (u'无', u'无'),
        (u'有', u'有'),
        (u'不详', u'不详'),
    )
    #是否为排卵障碍性
    OVULATION = (
        (u'是',u'是'),
        (u'否', u'否'),
        (u'不详', u'不详'),
    )

    person = models.OneToOneField(GeneralInfo, on_delete=models.CASCADE)
    person_born = models.CharField(verbose_name=u'出生情况',choices=BORNCOND, max_length=30)
    #special_hobbies = models.ForeignKey(OtherSpecialHobbies, on_delete=models.CASCADE)
    body_cond = models.CharField(verbose_name=u'体力状况',choices=BODYCOND, max_length=20)
    career_labor = models.CharField(verbose_name=u'职业体力活动',choices=CAREERLABOR, max_length=100)
    poor_blood = models.CharField(verbose_name=u'贫血与否', choices=POORBLOOD, max_length=20)
    phycial_exercise = models.CharField(verbose_name=u'体育锻炼', choices=PHYCIALEXER, max_length=50)
    #reduce_fat = models.ForeignKey(OtherReduceFat, on_delete=models.CASCADE)
    #mens_cond = models.ForeignKey(OtherMensCond, on_delete=models.CASCADE)
    #leucorrhea = models.ForeignKey(OtherLeucorrhea, on_delete=models.CASCADE)
    #past_history = models.ForeignKey(OtherPastHistory, on_delete=models.CASCADE)
    #past_mens = models.ForeignKey(OtherPastMenstruation, on_delete=models.CASCADE)
    womb_blood = models.CharField(verbose_name=u'一级亲属（母亲、姐妹、女儿）异常子宫出血史', choices=WOMBBLOOD, max_length=10)
    ovulation = models.CharField(verbose_name=u'是否为排卵障碍性', choices=OVULATION, max_length=10)
    #past_family = models.ForeignKey(OtherPastFamily, on_delete=models.CASCADE)
    #past_preg = models.ForeignKey(OtherPastPregnant, on_delete=models.CASCADE)
    #prevent_method = models.ForeignKey(OtherPrevent, on_delete=models.CASCADE)
    #accessory_check = models.ForeignKey(OtherAccessoryCheck, on_delete=models.CASCADE)

    class Meta:
        verbose_name = u'其它情况'

#其它-特殊嗜好
class OtherSpecialHobbies(models.Model):
    wu = models.BooleanField(verbose_name=u'无')
    xiyan = models.BooleanField(verbose_name=u'吸烟')
    yinjiu = models.BooleanField(verbose_name=u'饮酒')
    qita = models.BooleanField(verbose_name=u'其它')
    qita_desc = models.CharField(verbose_name=u'其它说明',max_length=100, default=u'无')

    other = models.OneToOneField(Other, on_delete=models.CASCADE)

    class Meta:
        verbose_name = u'特殊嗜好'

#其它-减肥情况
class OtherReduceFat(models.Model):
    ever = models.BooleanField(verbose_name=u'有减肥')
    yundong = models.BooleanField(verbose_name=u'运动减肥')
    jieshi = models.BooleanField(verbose_name=u'节食减肥')
    yaowu = models.BooleanField(verbose_name=u'药物减肥')
    qita = models.BooleanField(verbose_name=u'其它')
    qita_desc = models.CharField(verbose_name=u'其它说明', max_length=50, default=u'无')
    persist = models.IntegerField(verbose_name=u'减肥时长（月）', blank=True, null=True)

    other = models.OneToOneField(Other, on_delete=models.CASCADE)

    class Meta:
        verbose_name = u'减肥情况'

#其它-经期情况
class OtherMensCond(models.Model):
    CONDCHOICE = (
        (u'有',u'有'),
        (u'偶尔', u'偶尔'),
        (u'经常', u'经常'),
        (u'无', u'无'),
    )
    yundong = models.CharField(verbose_name=u'经期运动', choices=CONDCHOICE, max_length=10)
    ganmao = models.CharField(verbose_name=u'经期感冒', choices=CONDCHOICE, max_length=10)
    tongfang = models.CharField(verbose_name=u'经期同房', choices=CONDCHOICE, max_length=10)
    zhaoliang = models.CharField(verbose_name=u'经期着凉', choices=CONDCHOICE, max_length=10)

    other = models.OneToOneField(Other, on_delete=models.CASCADE)

    class Meta:
        verbose_name = u'经期情况'

#其它-平素带下情况
class OtherLeucorrhea(models.Model):
    liangshao = models.BooleanField(verbose_name=u'带下量少')
    liangke = models.BooleanField(verbose_name=u'带下量可')
    liangduo = models.BooleanField(verbose_name=u'带下量多')
    sehuang = models.BooleanField(verbose_name=u'带下色黄')
    sebai = models.BooleanField(verbose_name=u'带下色白')
    selv = models.BooleanField(verbose_name=u'带下色绿')
    zhiqingxi = models.BooleanField(verbose_name=u'带下质清稀')
    zhinianchou = models.BooleanField(verbose_name=u'带下质粘稠')

    other = models.OneToOneField(Other, on_delete=models.CASCADE)

    class Meta:
        verbose_name = u'平素带下情况'

#其它-既往病史
class OtherPastHistory(models.Model):
    wu = models.BooleanField(verbose_name=u'无')
    yuejingbutiao = models.BooleanField(verbose_name=u'月经不调')
    yindaoyan = models.BooleanField(verbose_name=u'阴道炎')
    zigongneimoyan = models.BooleanField(verbose_name=u'子宫内膜炎')
    zigongneimoyiwei = models.BooleanField(verbose_name=u'子宫内膜异位症')
    zigongxianjizheng = models.BooleanField(verbose_name=u'子宫腺肌症')
    penqiangyan = models.BooleanField(verbose_name=u'盆腔炎')
    zigongjiliu = models.BooleanField(verbose_name=u'子宫肌瘤')
    luancaonangzhong = models.BooleanField(verbose_name=u'卵巢囊肿')
    ruxianzengsheng = models.BooleanField(verbose_name=u'乳腺增生')
    jiazhuangxian = models.BooleanField(verbose_name=u'甲状腺相关疾病')
    shengzhiyichang = models.BooleanField(verbose_name=u'生殖器官发育异常')
    naochuitiliu = models.BooleanField(verbose_name=u'脑垂体瘤')
    feipang = models.BooleanField(verbose_name=u'肥胖')
    ganyan = models.BooleanField(verbose_name=u'肝炎')
    jiehe = models.BooleanField(verbose_name=u'结核')
    qita = models.BooleanField(verbose_name=u'其它')
    qita_desc = models.CharField(verbose_name=u'其它说明',max_length=100, default=u'无')

    other = models.OneToOneField(Other, on_delete=models.CASCADE)

    class Meta:
        verbose_name = u'既往病史'

#其它-月经不调病史
class OtherPastMenstruation(models.Model):
    zhouqiwenluan = models.BooleanField(verbose_name=u'月经周期紊乱')
    liangduo = models.BooleanField(verbose_name=u'月经量多')
    zhouqisuoduan = models.BooleanField(verbose_name=u'月经周期缩短')
    yanhou = models.BooleanField(verbose_name=u'月经延后')
    yanchang = models.BooleanField(verbose_name=u'行经期延长')
    tingbi = models.BooleanField(verbose_name=u'月经停闭')
    chuxie = models.BooleanField(verbose_name=u'经间期出血')

    other = models.OneToOneField(Other, on_delete=models.CASCADE)

    class Meta:
        verbose_name = u'月经不调病史'

#其它-家族史- 一级亲属（父母、兄弟姐妹、子女）其他疾病史
class OtherPastFamily(models.Model):
    wu = models.BooleanField(verbose_name=u'无')
    gaoxueya = models.BooleanField(verbose_name=u'高血压')
    tangniaobing = models.BooleanField(verbose_name=u'糖尿病')
    xinzangbing = models.BooleanField(verbose_name=u'心脏病')
    duonangluanchao = models.BooleanField(verbose_name=u'多囊卵巢综合征')
    buxiang = models.BooleanField(verbose_name=u'不详')
    qita = models.BooleanField(verbose_name=u'其它')
    qita_desc = models.CharField(verbose_name=u'其它说明',max_length=100, default=u'无')

    other = models.OneToOneField(Other, on_delete=models.CASCADE)

    class Meta:
        verbose_name = u'一级亲属其它病史'

#其它-孕育史
class OtherPastPregnant(models.Model):
    yuncount = models.IntegerField(verbose_name=u'孕次总数')
    pougong = models.IntegerField(verbose_name=u'剖宫产次数', blank=True, null=True)
    shunchan = models.IntegerField(verbose_name=u'顺产次数', blank=True, null=True)
    yaoliu = models.IntegerField(verbose_name=u'药物流产次数', blank=True, null=True)
    renliu = models.IntegerField(verbose_name=u'人工流产次数', blank=True, null=True)
    ziranliu = models.IntegerField(verbose_name=u'自然流产次数', blank=True, null=True)
    shenghuarenshen = models.IntegerField(verbose_name=u'生化妊娠次数', blank=True, null=True)
    yiweirenshen = models.IntegerField(verbose_name=u'异位妊娠次数', blank=True, null=True)
    taitingyu = models.IntegerField(verbose_name=u'胎停育次数', blank=True, null=True)
    qinggongshu = models.IntegerField(verbose_name=u'清宫术次数', blank=True, null=True)

    other = models.OneToOneField(Other, on_delete=models.CASCADE)

    class Meta:
        verbose_name = u'孕育史'

#其它-避孕措施
class OtherPrevent(models.Model):
    jieza = models.BooleanField(verbose_name=u'结扎')
    jieyuqi = models.BooleanField(verbose_name=u'宫内节育器')
    biyuntao = models.BooleanField(verbose_name=u'避孕套')
    biyunyao = models.BooleanField(verbose_name=u'口服避孕药')

    biyunyao_time = models.DecimalField(verbose_name=u'末次口服避孕药时间',max_digits=3,decimal_places=1, blank=True, null=True) #距离末次性行为之后多长时间服药
    mafulong = models.BooleanField(verbose_name=u'去氧孕烯炔雌片（妈富隆）')
    daying = models.BooleanField(verbose_name=u'炔雌醇环丙孕酮片（达英-35）')
    yousiming = models.BooleanField(verbose_name=u'屈螺酮炔雌醇片（优思明）')
    zuoque = models.BooleanField(verbose_name=u'左炔诺孕酮')
    fufang = models.BooleanField(verbose_name=u'复方左炔诺孕酮')
    qita = models.BooleanField(verbose_name=u'其它')
    qita_desc = models.CharField(verbose_name=u'其它说明', max_length=100, default=u'无')

    other = models.OneToOneField(Other, on_delete=models.CASCADE)

    class Meta:
        verbose_name = u'避孕措施'

#其它-辅助性检查
class OtherAccessoryCheck(models.Model):
    HGBVALUE = (
        (u'>110',u'>110'),
        (u'91-110', u'91-110'),
        (u'61-90', u'61-90'),
        (u'30-60', u'30-60'),
    )
    hgb_value = models.CharField(verbose_name=u'血红蛋白值', choices=HGBVALUE, max_length=20)
    quanxuexibaojishu = models.BooleanField(verbose_name=u'全血细胞计数')
    chuxuexingjibing = models.BooleanField(verbose_name=u'出血性疾病筛查（如女性血管性血友病）')
    ningxue = models.BooleanField(verbose_name=u'凝血功能检查')
    jiazhuangxian = models.BooleanField(verbose_name=u'甲状腺功能检测')
    niaorenshen = models.BooleanField(verbose_name=u'尿妊娠试验')
    penqiangchaosheng = models.BooleanField(verbose_name=u'盆腔超声检查')
    jichutiwen = models.BooleanField(verbose_name=u'基础体温测定')
    jisushuiping = models.BooleanField(verbose_name=u'激素水平测定')
    guagong = models.BooleanField(verbose_name=u'诊断性刮宫或宫腔镜下刮宫')
    qita = models.BooleanField(verbose_name=u'其它')
    qita_desc = models.CharField(verbose_name=u'其它说明', max_length=100, default=u'无')

    other = models.OneToOneField(Other, on_delete=models.CASCADE)

    class Meta:
        verbose_name = u'其它辅助检查'

################################################################################
#五、临床诊断
class ClinicalConclusion(models.Model):
    person = models.OneToOneField(GeneralInfo, on_delete=models.CASCADE)
    serial = models.IntegerField(verbose_name=u'临床诊断对应患者编号', default=-1)
    #chinese_conclusion = models.ForeignKey(ChineseConclusion, on_delete=models.CASCADE)
    #asthenic = models.ForeignKey(Asthenic, on_delete=models.CASCADE)
    #demonstration = models.ForeignKey(Demonstration, on_delete=models.CASCADE)
    #deficiency_excess = models.ForeignKey(DeficiencyExcess, on_delete=models.CASCADE)
    #west_conclusion = models.ForeignKey(WestConclusion, on_delete=models.CASCADE)

    class Meta:
        verbose_name = u'临床诊断'

#五、临床诊断-中医诊断
class ChineseConclusion(models.Model):
    benglou = models.BooleanField(verbose_name=u'崩漏')
    yuejingguoduo = models.BooleanField(verbose_name=u'月经过多')
    yuejingxianqi = models.BooleanField(verbose_name=u'月经先期')
    jingqiyanchang = models.BooleanField(verbose_name=u'经期延长')
    jingjianqichuxie = models.BooleanField(verbose_name=u'经间期出血')

    conclusion = models.OneToOneField(ClinicalConclusion, on_delete=models.CASCADE)

    class Meta:
        verbose_name = u'中医诊断'

#临床诊断-辩证分型-虚证
class Asthenic(models.Model):
    shenyin = models.BooleanField(verbose_name=u'肾阴虚证')
    shenyang = models.BooleanField(verbose_name=u'肾阳虚证')
    shenqi = models.BooleanField(verbose_name=u'肾气虚证')
    piqi = models.BooleanField(verbose_name=u'脾气虚证')
    qixuxiaxian = models.BooleanField(verbose_name=u'气虚下陷证')
    xure = models.BooleanField(verbose_name=u'虚热证')
    xinpiliangxu = models.BooleanField(verbose_name=u'心脾两虚证')
    pishenyangxu = models.BooleanField(verbose_name=u'脾肾阳虚证')
    qixuekuixu = models.BooleanField(verbose_name=u'气血亏虚症')
    ganshenyinxu = models.BooleanField(verbose_name=u'肝肾阴虚证')
    qita = models.BooleanField(verbose_name=u'其它')
    qita_desc = models.CharField(verbose_name=u'其它说明', max_length=50, default=u'无')

    conclusion = models.OneToOneField(ClinicalConclusion, on_delete=models.CASCADE)

    class Meta:
        verbose_name = u'辩证分型-虚证'

#临床诊断-辩证分型-实证
class Demonstration(models.Model):
    ganyuxuere = models.BooleanField(verbose_name=u'肝郁血热证')
    yangshengxuere = models.BooleanField(verbose_name=u'阳盛血热证')
    ganjingshire = models.BooleanField(verbose_name=u'肝经湿热证')
    tanreyuzu = models.BooleanField(verbose_name=u'痰热瘀阻证')
    tanshizuzhi = models.BooleanField(verbose_name=u'痰湿阻滞证')
    tanyuzuzhi = models.BooleanField(verbose_name=u'痰瘀阻滞证')
    yurehujie = models.BooleanField(verbose_name=u'瘀热互结证')
    xueyu = models.BooleanField(verbose_name=u'血瘀证')
    qizhixueyu = models.BooleanField(verbose_name=u'气滞血瘀证')
    hanningxueyu = models.BooleanField(verbose_name=u'寒凝血淤症')
    qita = models.BooleanField(verbose_name=u'其它')
    qita_desc = models.CharField(verbose_name=u'其它说明',max_length=50, default=u'无')

    conclusion = models.OneToOneField(ClinicalConclusion, on_delete=models.CASCADE)

    class Meta:
        verbose_name = u'辩证分型-实证'

#临床诊断-辩证分型-虚实夹杂证
class DeficiencyExcess(models.Model):
    shenxuxueyu = models.BooleanField(verbose_name=u'肾虚血瘀证')
    shenxuyure = models.BooleanField(verbose_name=u'肾虚瘀热证')
    shenxuganyu = models.BooleanField(verbose_name=u'肾虚肝郁证')
    qixuxueyu = models.BooleanField(verbose_name=u'气虚血瘀证')
    yinxuxueyu = models.BooleanField(verbose_name=u'阴虚血瘀证')
    yinxuhuowang = models.BooleanField(verbose_name=u'阴虚火旺证')
    ganyupixu = models.BooleanField(verbose_name=u'肝郁脾虚证')
    qita = models.BooleanField(verbose_name=u'其它')
    qita_desc = models.CharField(verbose_name=u'其它说明', max_length=50, default=u'无')

    conclusion = models.OneToOneField(ClinicalConclusion, on_delete=models.CASCADE)

    class Meta:
        verbose_name = u'辩证分型-虚实夹杂'

#临床诊断-西医诊断
class WestConclusion(models.Model):
    duonangluanchao = models.BooleanField(verbose_name=u'多囊卵巢综合征')
    gaomirusu = models.BooleanField(verbose_name=u'高泌乳素血症')
    dicuxingxianjisu = models.BooleanField(verbose_name=u'低促行线激素疾病')
    qita = models.BooleanField(verbose_name=u'其它')
    qita_desc = models.CharField(verbose_name=u'其它说明', max_length=50, default=u'无')

    conclusion = models.OneToOneField(ClinicalConclusion, on_delete=models.CASCADE)

    class Meta:
        verbose_name = u'西医诊断'

