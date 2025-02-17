import pyvisa as visa
import pandas as pd
import time

class AWG_DG4162:
    def __init__(self, resource_name):
        """
        初始化信号源对象。
        :param resource_name: 信号源的VISA资源名称。
        """
        self.resource_name = resource_name
        self.rm = visa.ResourceManager()
        self.instrument = self.rm.open_resource(self.resource_name)

    def reset(self):
        """
        仪器重置
        """
        self.instrument.write("*RST")
        #self.instrument.write(":SYSTem:PRESet DEFault")

    def query_ID(self):
        """
        解释：查询仪器ID
        """
        return self.instrument.query("*IDN?")


    def output1(self):
        """
        打开通道1，输出信号
        """
        self.instrument.write(":OUTPut1 ON")

    def output2(self):
        """
        打开通道1，输出信号
        """
        self.instrument.write(":OUTPut2 ON")
    ################################################################################
    #    设置输出阻抗
    ################################################################################

    def set_ch1_impedance(self,impedance):
        """
        设置通道1输出阻抗,单位Ω，高阻设置‘INFinity’
        """
        command = f":OUTPut1:IMPedance {impedance}"
        self.instrument.write(command)

    def set_ch2_impedance(self,impedance):
        """
        设置通道2输出阻抗,单位Ω，高阻设置‘INFinity’
        """
        command = f":OUTPut2:IMPedance {impedance}"
        self.instrument.write(command)
    ################################################################################
    #    设置输出电平 成对设置，vpp和offset一对，highlevel和lowlevel一对，互斥
    ################################################################################
    def set_ch1_vpp(self,vpp):
        """
        设置通道1输出峰峰值电压,单位V，格式：[:SOURce<n>]:VOLTage[:LEVel][:IMMediate][:AMPLitude] <amplitude>|MINimum|MAXimum
        """
        command = f":SOURce1:VOLTage {vpp}"
        self.instrument.write(command)

    def set_ch2_vpp(self,vpp):
        """
        设置通道2输出峰峰值电压,单位V，格式：[:SOURce<n>]:VOLTage[:LEVel][:IMMediate][:AMPLitude] <amplitude>|MINimum|MAXimum
        """
        command = f":SOURce2:VOLTage {vpp}"
        self.instrument.write(command)

    def set_ch1_highlevel(self,high):
        """
        设置通道1输出高电平,单位V，格式：[:SOURce<n>]:VOLTage[:LEVel][:IMMediate]:HIGH <voltage>|MINimum|MAXimum
        """
        command = f":SOURce1:VOLTage:HIGH {high}"
        self.instrument.write(command)

    def set_ch2_highlevel(self,high):
        """
        设置通道2输出高电平,单位V，格式：[:SOURce<n>]:VOLTage[:LEVel][:IMMediate]:HIGH <voltage>|MINimum|MAXimum
        """
        command = f":SOURce2:VOLTage:HIGH {high}"
        self.instrument.write(command)

    def set_ch1_lowlevel(self,low):
        """
        设置通道1输出低电平,单位V，格式：[:SOURce<n>]:VOLTage[:LEVel][:IMMediate]:LOW <voltage>|MINimum|MAXimum
        """
        command = f":SOURce1:VOLTage:LOW {low}"
        self.instrument.write(command)

    def set_ch2_lowlevel(self,low):
        """
        设置通道2输出低电平,单位V，格式：[:SOURce<n>]:VOLTage[:LEVel][:IMMediate]:LOW <voltage>|MINimum|MAXimum
        """
        command = f":SOURce2:VOLTage:LOW {low}"
        self.instrument.write(command)

    def set_ch1_offset(self,offset):
        """
        设置通道1输出电平偏置,单位V，格式：[:SOURce<n>]:VOLTage[:LEVel][:IMMediate]:OFFSet <voltage>|MINimum|MAXimum
        """
        command = f":SOURce1:VOLTage:OFFSet {offset}"
        self.instrument.write(command)

    def set_ch2_offset(self,offset):
        """
        设置通道1输出电平偏置,单位V，格式：[:SOURce<n>]:VOLTage[:LEVel][:IMMediate]:OFFSet <voltage>|MINimum|MAXimum
        """
        command = f":SOURce2:VOLTage:OFFSet {offset}"
        self.instrument.write(command)
    ################################################################################
    #    设置正弦波参数
    ################################################################################
    def set_ch1_sine(self, freq,amp,offset,phase):
        """
        设置正弦波形，格式[:SOURce<n>]:APPLy:SINusoid [<freq>[,<amp>[,<offset>[,<phase>]]]]
        默认：[<freq>[,<amp>[,<offset>[,<phase>]=[1kHz,5Vpp,0Vdc,0°]
        单位: freq单位为赫兹(Hz)，amp单位为伏特(V)，offset单位为伏特(V),phase单位为伏特(°)
        """
        command = f":SOURce1:APPLy:SINusoid {freq},{amp},{offset},{phase}"
        self.instrument.write(command)

    def set_ch2_sine(self, freq,amp,offset,phase):
        """
        设置正弦波形，格式[:SOURce<n>]:APPLy:SINusoid [<freq>[,<amp>[,<offset>[,<phase>]]]]
        默认：[<freq>[,<amp>[,<offset>[,<phase>]=[1kHz,5Vpp,0Vdc,0°]
        单位: freq单位为赫兹(Hz)，amp单位为伏特(V)，offset单位为伏特(V),phase单位为伏特(°)
        """
        command = f":SOURce2:APPLy:SINusoid {freq},{amp},{offset},{phase}"
        self.instrument.write(command)
    ################################################################################
    #    设置方波参数
    ################################################################################
    def set_ch1_square(self, freq,amp,offset,phase):
        """
        设置方波，格式[:SOURce<n>]:APPLy:SQUare [<freq>[,<amp>[,<offset>[,<phase>]]]]
        默认：[<freq>[,<amp>[,<offset>[,<phase>]=[1kHz,5Vpp,0Vdc,0°]
        单位: freq单位为赫兹(Hz)，amp单位为伏特(V)，offset单位为伏特(V),phase单位为伏特(°)
        """
        command = f":SOURce1:APPLy:SQUare {freq},{amp},{offset},{phase}"
        self.instrument.write(command)

    def set_ch2_square(self, freq,amp,offset,phase):
        """
        设置方波，格式[:SOURce<n>]:APPLy:SQUare [<freq>[,<amp>[,<offset>[,<phase>]]]]
        默认：[<freq>[,<amp>[,<offset>[,<phase>]=[1kHz,5Vpp,0Vdc,0°]
        单位: freq单位为赫兹(Hz)，amp单位为伏特(V)，offset单位为伏特(V),phase单位为伏特(°)
        """
        command = f":SOURce2:APPLy:SQUare {freq},{amp},{offset},{phase}"
        self.instrument.write(command)
    ################################################################################
    #    设置脉冲参数
    ################################################################################
    def set_ch1_pulse(self, freq,amp,offset,phase):
        """
        设置脉冲波形，格式[:SOURce<n>]:APPLy:PULSe [<freq>[,<amp>[,<offset>[,<delay>]]]]
        默认：[<freq>[,<amp>[,<offset>[,<phase>]=[1kHz,5Vpp,0Vdc,0°]
        单位: freq单位为赫兹(Hz)，amp单位为伏特(V)，offset单位为伏特(V),phase单位为°
        """
        command = f":SOURce1:APPLy:PULSe {freq},{amp},{offset},{phase}"
        self.instrument.write(command)

    def set_ch2_pulse(self, freq,amp,offset,delay):
        """
        设置脉冲波形，格式[:SOURce<n>]:APPLy:PULSe [<freq>[,<amp>[,<offset>[,<delay>]]]]
        默认：[<freq>[,<amp>[,<offset>[,<phase>]=[1kHz,5Vpp,0Vdc,0°]
        单位: freq单位为赫兹(Hz)，amp单位为伏特(V)，offset单位为伏特(V),phase单位为°
        """
        command = f":SOURce2:APPLy:PULSe {freq},{amp},{offset},{delay}"
        self.instrument.write(command)

    def set_pulse1_dutycycle(self, percent):
        """
        设置脉冲占空比，格式[:SOURce<n>]:PULSe:DCYCle <percent>|MINimum|MAXimum
        默认：占空比50%,脉冲占空比受“最小脉冲宽度（4 ns）”和“脉冲周期”限制
        脉冲占空比 ≥ 100 × 最小脉冲宽度 ÷ 脉冲周期 脉冲占空比 ≤ 100 ×（1 - 2 × 最小脉冲宽度 ÷ 脉冲周期）
        """
        command = f":SOURce1:PULSe:DCYCle {percent}"
        self.instrument.write(command)

    def set_pulse2_dutycycle(self, percent):
        """
        设置脉冲占空比，格式[:SOURce<n>]:PULSe:DCYCle <percent>|MINimum|MAXimum
        默认：占空比50%,脉冲占空比受“最小脉冲宽度（4 ns）”和“脉冲周期”限制
        脉冲占空比 ≥ 100 × 最小脉冲宽度 ÷ 脉冲周期 脉冲占空比 ≤ 100 ×（1 - 2 × 最小脉冲宽度 ÷ 脉冲周期）
        """
        command = f":SOURce2:PULSe:DCYCle {percent}"
        self.instrument.write(command)

    def set_pulse1_delay(self, delay):
        """
        设置脉冲占空比，格式[:SOURce<n>]:PULSe:DELay <delay>|MINimum|MAXimum
        默认：0ns  单位: s
        """
        command = f":SOURce1:PULSe:DELay {delay}"
        self.instrument.write(command)

    def set_pulse2_delay(self, delay):
        """
        设置脉冲占空比，格式[:SOURce<n>]:PULSe:DELay <delay>|MINimum|MAXimum
        默认：0ns 单位: s
        """
        command = f":SOURce2:PULSe:DELay {delay}"
        self.instrument.write(command)

    def set_pulse1_hold(self, parameter):
        """
        设置脉冲占空比，格式[:SOURce<n>]:PULSe:HOLD WIDTh|DUTY
        说明：选中脉冲波的脉宽或占空比不变，WIDTh|DUTY
        """
        command = f":SOURce1:PULSe:HOLD {parameter}"
        self.instrument.write(command)

    def set_pulse2_hold(self, parameter):
        """
        设置脉冲占空比，格式[:SOURce<n>]:PULSe:HOLD WIDTh|DUTY
        说明：选中脉冲波的脉宽或占空比不变，WIDTh|DUTY
        """
        command = f":SOURce2:PULSe:HOLD {parameter}"
        self.instrument.write(command)

    def set_pulse1_rising_edge(self, seconds):
        """
        设置脉冲上升沿，格式[:SOURce<n>]:PULSe:TRANsition:LEADing <seconds>|MINimum|MAXimum
        说明：设置脉冲上升沿时间，单位默认为“s”。可设置范围受当前指定的脉宽限制，
        限制关系为满足不等式：上升/下降沿时间 ≤ 0.625 × 脉宽,当所设置的数值超出限定值，DG4000自动调整边沿时间以适应指定的脉宽。
        """
        command = f":SOURce1:PULSe:TRANsition:LEADing {seconds}"
        self.instrument.write(command)

    def set_pulse2_rising_edge(self, seconds):
        """
        设置脉冲上升沿，格式[:SOURce<n>]:PULSe:TRANsition:LEADing <seconds>|MINimum|MAXimum
        说明：设置脉冲上升沿时间，单位默认为“s”。可设置范围受当前指定的脉宽限制，
        限制关系为满足不等式：上升/下降沿时间 ≤ 0.625 × 脉宽,当所设置的数值超出限定值，DG4000自动调整边沿时间以适应指定的脉宽。
        """
        command = f":SOURce2:PULSe:TRANsition:LEADing {seconds}"
        self.instrument.write(command)

    def set_pulse1_falling_edge(self, seconds):
        """
        设置脉冲下降沿，格式[:SOURce<n>]:PULSe:TRANsition:TRAiling <seconds>|MINimum|MAXimum
        说明：设置脉冲上升沿时间，单位默认为“s”。可设置范围受当前指定的脉宽限制，
        限制关系为满足不等式：上升/下降沿时间 ≤ 0.625 × 脉宽,当所设置的数值超出限定值，DG4000自动调整边沿时间以适应指定的脉宽。
        """
        command = f":SOURce1:PULSe:TRANsition:TRAiling {seconds}"
        self.instrument.write(command)

    def set_pulse2_falling_edge(self, seconds):
        """
        设置脉冲下降沿，格式[:SOURce<n>]:PULSe:TRANsition:TRAiling <seconds>|MINimum|MAXimum
        说明：设置脉冲上升沿时间，单位默认为“s”。可设置范围受当前指定的脉宽限制，
        限制关系为满足不等式：上升/下降沿时间 ≤ 0.625 × 脉宽,当所设置的数值超出限定值，DG4000自动调整边沿时间以适应指定的脉宽。
        """
        command = f":SOURce2:PULSe:TRANsition:TRAiling {seconds}"
        self.instrument.write(command)

    def set_pulse1_width(self, seconds):
        """
        设置脉冲宽度，格式[:SOURce<n>]:PULSe:WIDTh <seconds>|MINimum|MAXimum
        说明：与占空比相关联，修改其中一个参数将自动修改另一个参数，受“最小脉冲宽度（4 ns）”和“脉冲周期”的限制。
        脉冲宽度 ≥ 最小脉冲宽度     脉冲宽度 ≤ 脉冲周期 - 2 × 最小脉冲宽度
        """
        command = f":SOURce1:PULSe:WIDTh {seconds}"
        self.instrument.write(command)

    def set_pulse2_width(self, seconds):
        """
        设置脉冲宽度，格式[:SOURce<n>]:PULSe:WIDTh <seconds>|MINimum|MAXimum
        说明：与占空比相关联，修改其中一个参数将自动修改另一个参数，受“最小脉冲宽度（4 ns）”和“脉冲周期”的限制。
        脉冲宽度 ≥ 最小脉冲宽度     脉冲宽度 ≤ 脉冲周期 - 2 × 最小脉冲宽度
        """
        command = f":SOURce2:PULSe:WIDTh {seconds}"
        self.instrument.write(command)

    ################################################################################
    #    设置锯齿波波形参数
    ################################################################################
    def set_ch1_sawtooth(self, freq,amp,offset,phase):
        """
        设置AWG波形，格式[:SOURce<n>]:APPLy:RAMP [<freq>[,<amp>[,<offset>[,<phase>]]]]
        默认：[<freq>[,<amp>[,<offset>[,<phase>]=[1kHz,5Vpp,0Vdc,0°]
        单位: freq单位为赫兹(Hz)，amp单位为伏特(V)，offset单位为伏特(V),phase单位为伏特(°)
        """
        command = f":SOURce1:APPLy:RAMP {freq},{amp},{offset},{phase}"
        self.instrument.write(command)

    def set_ch2_sawtooth(self, freq,amp,offset,phase):
        """
        设置AWG波形，格式[:SOURce<n>]:APPLy:RAMP [<freq>[,<amp>[,<offset>[,<phase>]]]]
        默认：[<freq>[,<amp>[,<offset>[,<phase>]=[1kHz,5Vpp,0Vdc,0°]
        单位: freq单位为赫兹(Hz)，amp单位为伏特(V)，offset单位为伏特(V),phase单位为伏特(°)
        """
        command = f":SOURce2:APPLy:RAMP {freq},{amp},{offset},{phase}"
        self.instrument.write(command)

    def set_sawtooth1_symmetry(self, persent):
        """
        设置AWG波形，格式[:SOURce<n>]:FUNCtion:RAMP:SYMMetry <symmetry>|MINimum|MAXimum
        默认：50%
        """
        command = f":SOURce1:FUNCtion:RAMP:SYMMetry {persent}"
        self.instrument.write(command)

    def set_sawtooth2_symmetry(self, persent):
        """
        设置AWG波形，格式[:SOURce<n>]:FUNCtion:RAMP:SYMMetry <symmetry>|MINimum|MAXimum
        默认：50%
        """
        command = f":SOURce2:FUNCtion:RAMP:SYMMetry {persent}"
        self.instrument.write(command)
    ################################################################################
    #    设置自定义波形参数
    ################################################################################
    def set_ch1_customwave(self, freq,amp,offset,phase):
        """
        设置AWG波形，格式[:SOURce<n>]:APPLy:CUSTom [<freq>[,<amp>[,<offset>[,<phase>]]]]。
        默认：[<freq>[,<amp>[,<offset>[,<phase>]=[1kHz,5Vpp,0Vdc,0°]
        单位: freq单位为赫兹(Hz)，amp单位为伏特(V)，offset单位为伏特(V),phase单位为伏特(°)
        """
        command = f":SOURce1:APPLy:CUSTom {freq},{amp},{offset},{phase}"

    def set_ch2_customwave(self, freq,amp,offset,phase):
        """
        设置AWG波形，格式[:SOURce<n>]:APPLy:CUSTom [<freq>[,<amp>[,<offset>[,<phase>]]]]。
        默认：[<freq>[,<amp>[,<offset>[,<phase>]=[1kHz,5Vpp,0Vdc,0°]
        单位: freq单位为赫兹(Hz)，amp单位为伏特(V)，offset单位为伏特(V),phase单位为伏特(°)
        """
        command = f":SOURce2:APPLy:CUSTom {freq},{amp},{offset},{phase}"

    def set_ch1_userwave(self, freq,amp,offset,phase):
        """
        设置AWG波形，格式[:SOURce<n>]:APPLy:CUSTom [<freq>[,<amp>[,<offset>[,<phase>]]]]。
        默认：[<freq>[,<amp>[,<offset>[,<phase>]=[1kHz,5Vpp,0Vdc,0°]
        单位: freq单位为赫兹(Hz)，amp单位为伏特(V)，offset单位为伏特(V),phase单位为伏特(°)
        """
        command = f":SOURce1:APPLy:USER {freq},{amp},{offset},{phase}"
        self.instrument.write(command)

    def set_ch2_userwave(self, freq,amp,offset,phase):
        """
        设置AWG波形，格式[:SOURce<n>]:APPLy:CUSTom [<freq>[,<amp>[,<offset>[,<phase>]]]]。
        默认：[<freq>[,<amp>[,<offset>[,<phase>]=[1kHz,5Vpp,0Vdc,0°]
        单位: freq单位为赫兹(Hz)，amp单位为伏特(V)，offset单位为伏特(V),phase单位为伏特(°)
        """
        command = f":SOURce2:APPLy:USER {freq},{amp},{offset},{phase}"
        self.instrument.write(command)
    ################################################################################
    #    设置谐波波形参数
    ################################################################################
    def set_ch1_harmonic(self, freq,amp,offset,phase):
        """
        设置谐波波形，格式[:SOURce<n>]:APPLy:HARMonic [<freq>[,<amp>[,<offset>[,<phase>]]]]
        默认：[<freq>[,<amp>[,<offset>[,<phase>]=[1kHz,5Vpp,0Vdc,0°]
        范围: DG4162在阻抗为“高阻”，谐波次数为“2”时的范围。1 μHz至80 MHz
        """
        command = f":SOURce1:APPLy:HARMonic {freq},{amp},{offset},{phase}"
        self.instrument.write(command)

    def set_ch2_harmonic(self, freq,amp,offset,phase):
        """
        设置谐波波形，格式[:SOURce<n>]:APPLy:HARMonic [<freq>[,<amp>[,<offset>[,<phase>]]]]
        默认：[<freq>[,<amp>[,<offset>[,<phase>]=[1kHz,5Vpp,0Vdc,0°]
        范围: DG4162在阻抗为“高阻”，谐波次数为“2”时的范围。1 μHz至80 MHz
        """
        command = f":SOURce2:APPLy:HARMonic {freq},{amp},{offset},{phase}"
        self.instrument.write(command)

    def set_ch1_harmonic_type(self, order):
        """
        设置谐波次数，格式[:SOURce<n>]:HARMonic:TYPe EVEN|ODD|ALL|USER
        默认：EVEN
        """
        command = f":SOURce1:HARMonic:TYPe {order}"
        self.instrument.write(command)

    def set_ch2_harmonic_type(self, order):
        """
        设置谐波次数，格式[:SOURce<n>]:HARMonic:TYPe EVEN|ODD|ALL|USER
        默认：EVEN
        """
        command = f":SOURce2:HARMonic:TYPe {order}"
        self.instrument.write(command)

    def set_ch1_harmonic_order(self, order):
        """
        设置谐波次数，格式[:SOURce<n>]:HARMonic:ORDEr <value>|MINimum|MAXimum
        默认：2
        """
        command = f":SOURce1:HARMonic:ORDEr {order}"
        self.instrument.write(command)

    def set_ch2_harmonic_order(self, order):
        """
        设置谐波次数，格式[:SOURce<n>]:HARMonic:ORDEr <value>|MINimum|MAXimum
        默认：2
        """
        command = f":SOURce2:HARMonic:ORDEr {order}"
        self.instrument.write(command)

    def set_ch1_harmonic_amp(self, sn,amp):
        """
        设置n次谐波幅度，格式[:SOURce<n>]:HARMonic:AMPL <sn>,<value>|MINimum|MAXimum
        """
        command = f":SOURce1:HARMonic:AMPL {sn},{amp}"
        self.instrument.write(command)

    def set_ch2_harmonic_amp(self, sn,amp):
        """
        设置n次谐波幅度，格式[:SOURce<n>]:HARMonic:AMPL <sn>,<value>|MINimum|MAXimum
        """
        command = f":SOURce2:HARMonic:AMPL {sn},{amp}"
        self.instrument.write(command)

    def set_ch1_harmonic_user(self, order):
        """
        用户定义n次谐波输出，格式[:SOURce<n>]:HARMonic:USER <user>
        说明： X000000000000000至X111111111111111
        最左侧的位表示基波，固定为X，不允许修改，后面的15位从左到右依次对应2次谐波到16次谐波。
        1表示打开相应次谐波的输出，0表示关闭相应次谐波的输出。
        """
        command = f":SOURce1:HARMonic:USER {order}"
        self.instrument.write(command)

    def set_ch2_harmonic_user(self, order):
        """
        用户定义n次谐波输出，格式[:SOURce<n>]:HARMonic:USER <user>
        说明： X000000000000000至X111111111111111
        最左侧的位表示基波，固定为X，不允许修改，后面的15位从左到右依次对应2次谐波到16次谐波。
        1表示打开相应次谐波的输出，0表示关闭相应次谐波的输出。
        """
        command = f":SOURce2:HARMonic:USER {order}"
        self.instrument.write(command)

    def set_ch1_harmonic_phase(self, sn, phase):
        """
        设置指定次谐波的相位，格式[:SOURce<n>]:HARMonic:PHASe <sn>,<value>|MINimum|MAXimum
        """
        command = f":SOURce1:HARMonic:PHASe {sn}, {phase}"
        self.instrument.write(command)

    def set_ch2_harmonic_phase(self, sn, phase):
        """
        设置指定次谐波的相位，格式[:SOURce<n>]:HARMonic:PHASe <sn>,<value>|MINimum|MAXimum
        """
        command = f":SOURce2:HARMonic:PHASe {sn}, {phase}"
        self.instrument.write(command)

    ################################################################################
    #    调整初始相位输出
    ################################################################################
    def set_ch1_phase(self, phase):
        """
        设置基本波的起始相位，格式[:SOURce<n>]:PHASe[:ADJust] <phase>|MINimum|MAXimum
        默认：0
        """
        command = f":SOURce1:PHASe:ADJust {phase}"
        self.instrument.write(command)

    def set_ch2_phase(self, phase):
        """
        设置基本波的起始相位，格式[:SOURce<n>]:PHASe[:ADJust] <phase>|MINimum|MAXimum
        默认：0
        """
        command = f":SOURce2:PHASe:ADJust {phase}"
        self.instrument.write(command)
    ################################################################################
    #    设置噪声输出
    ################################################################################
    def set_ch1_noise(self, amp, offset):
        """
        设置噪声波形，格式[:SOURce<n>]:APPLy:NOISe [<amp>[,<offset>]]
        默认：5Vpp，0V offset
        """
        command = f":SOURce1:APPLy:NOISe {amp},{offset}"
        self.instrument.write(command)

    def set_ch2_noise(self, amp, offset):
        """
        设置噪声波形，格式[:SOURce<n>]:APPLy:NOISe [<amp>[,<offset>]]
        默认：5Vpp，0V offset
        """
        command = f":SOURce2:APPLy:NOISe {amp},{offset}"
        self.instrument.write(command)
    ################################################################################
    #    系统操作
    ################################################################################
    def ch1_copyto_ch2(self):
        """
        将CH1的配置状态复制到CH2，格式:SYSTem:CSCopy CH1,CH2|CH2,CH1
        """
        command = f":SYSTem:CSCopy  CH1,CH2"
        self.instrument.write(command)

    def ch2_copyto_ch1(self):
        """
        将CH2的配置状态复制到CH1，格式: :SYSTem:CSCopy CH1,CH2|CH2,CH1
        """
        command = f":SYSTem:CSCopy  CH2,CH1"
        self.instrument.write(command)

    def set_ref_clk(self,status):
        """
        设置参考时钟源的类型为内部（INTernal）或外部（EXTernal），格式: :SYSTem:ROSCillator:SOURce INTernal|EXTernal
        """
        command = f":SYSTem:ROSCillator:SOURce {status}"
        self.instrument.write(command)

    def close(self):
        """
        关闭与信号源的连接。
        """
        self.instrument.close()
        self.rm.close()