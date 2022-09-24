## Projeto de Internet das Coisas em um Mundo Conectado

### Requisitos de Usuário
1. O sistema monitora a temperatura de duas estufas distintas;
2. As temperaturas são exibidas em graus Celsius (˚C);
3. Há um painel (dashboard) que pode ser visualizado em um Tablet ou computador,
exibindo a informação de cada estufa. Neste painel também há um botão que
permite habilitar ou não o controle de temperatura das duas estufas;
4. O sistema mantém a temperatura próxima aos 30˚C (temperatura ideal).

### Requisitos de Sistema
1. Em cada estufa há um dispositivo IoT com um sensor de temperatura1
;
2. Para esta implementação, o dispositivo IoT (device) utilizado é seu próprio PC
(execute dois projetos simultaneamente, um para cada dispositivo);
3. Cada dispositivo IoT transmite para o serviço em nuvem a temperatura do interior
da estufa;
4. Cada dispositivo IoT controla o aquecedor de sua estufa;
5. Há um painel único que mostra a temperatura das duas estufas;
6. O sensor de temperatura usado deve ser simulado. O valor da temperatura pode aumentar gradualmente
enquanto o relé do aquecedor está ligado, e reduzir gradualmente quando está desligado;
7. Em cada dispositivo IoT há um relé que liga e desliga um aquecedor na estufa (o relé
é também simulado). O valor da temperatura pode aumentar gradualmente enquanto o
relé do aquecedor está ligado, e reduzir gradualmente quando está desligado;
8. O painel contém um botão que permite habilitar ou não o controle do relé do
dispositivo IoT associado a este painel;
9. O relé do dispositivo é acionado apenas se a temperatura daquela estufa for inferior
a temperatura ideal e o botão do painel estiver ligado (habilitado);
10. O protocolo de comunicação a ser utilizado deve ser o MQTT;
11. O serviço em nuvem utilizado será o Cayenne myDevices
(www.cayenne.mydevices.com);