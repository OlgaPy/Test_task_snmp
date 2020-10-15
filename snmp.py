# import section
import re

from pysnmp.entity.rfc3413.oneliner import cmdgen
from ToBD import SQLITE


class SNMP_PY():

    def __init__(self):
        self.sql = SQLITE()
        #snmp
        #данные из файла с тестовым заданием
        self.community_string = 'public'
        self.ip_address_host = '192.168.2.2'
        self.port_snmp = 161        #порт по умолчанию для snmp
        self.oid= '1.3.6.1.2.1.31.1.1.1.1'
        self.speedOid = '1.3.6.1.2.1.2.2.1.5'
        self.openPortOid = '1.3.6.1.2.1.2.2.1.8'


    def check_physical(self, oid, value):       #ф-я проверки порта
        check = re.match(r'1\/\d+', value)      #подходит ли имя под конструкцию 1/число
        if (check != None):
            try:
                speedOid = oid.replace('SNMPv2-SMI::mib-2.31.1.1.1.1', 'SNMPv2-SMI::mib-2.2.2.1.5')     #получаем oid для получения скорости для этого порта
                openOid = oid.replace('SNMPv2-SMI::mib-2.31.1.1.1.1', 'SNMPv2-SMI::mib-2.2.2.1.8') #и для статуса
                print(value, self.dictSpeed[speedOid], self.dictOpen[openOid])
                self.sql.insert_port_data(value, self.dictSpeed[speedOid], self.dictOpen[openOid]) #запись в БД
                print('here')
            except Exception as ex:                                                             # или вывод текста ошибки
                print(ex)


    def get_walk(self, oid):                #запись в словарь данных по запрошенному OID, результат выполнения snmp_walk
        try:
            cmdGen = cmdgen.CommandGenerator()
            dataDict = {}
            errorIndication, errorStatus, errorIndex, varBindTable = cmdGen.nextCmd(
                cmdgen.CommunityData(self.community_string, mpModel=1),
                cmdgen.UdpTransportTarget((self.ip_address_host, self.port_snmp)),
                oid
            )

            if errorIndication:
                print(errorIndication)
                return None
            else:
                if errorStatus:
                    print('%s at %s' % (
                        errorStatus.prettyPrint(),
                        errorIndex and varBindTable[-1][int(errorIndex)-1] or '?'
                    )
                          )
                    return None
                else:                           #если нет ошибок в полученном ответе - записываем все параметры в словарь
                    for varBindTableRow in varBindTable:
                        for name, val in varBindTableRow:
                            dataDict[name.prettyPrint()] = val.prettyPrint()
                    return dataDict
        except Exception as ex: #todo сделать обработку исключений согласано библиотеки
            print(ex)

    def get_ports_info(self):                               #будем считывать информацию об коммутаторе
        self.physic = {}                                    #имена портов
        self.dictSpeed = {}                                 # их скорость
        self.dictOpen = {}                                  #х статус
        self.physic = self.get_walk(self.oid)               # выполняем snmpwalk для трех OIDов
        self.dictSpeed = self.get_walk(self.speedOid)
        self.dictOpen = self.get_walk(self.openPortOid)
        if self.physic == None or self.dictOpen == None or self.dictSpeed == None: # проверка на корректность ответа
            exit(-1)
        for key, value in self.physic.items():              #для всех элементов в словаре
            self.check_physical(key, value)                 #проверки физический ли порт

    #часть 2
    def get_ports_more_100(self):
        data = self.sql.select_port_more_100()
        print(data)

if __name__ == '__main__':
    snmp = SNMP_PY()                                        # создаем объект собственного класса
    snmp.get_ports_info()                                   # вызываем функцию получения информации о портах