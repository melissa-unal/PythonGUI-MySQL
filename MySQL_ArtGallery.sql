CREATE DATABASE Galerie_de_Arta;
create table GALERIE
(
cod_galerie integer,
nume_galerie varchar(30),
email char(20) unique,
constraint pk_cod_galerie primary key (cod_galerie)
);

alter table GALERIE
drop column email;

alter table GALERIE
add telefon varchar(20) unique;

create table ARTIST
(
cod_artist integer,
nume_artist varchar(50) not null,
prenume_artist varchar(15) not null,
tara varchar(30) not null,
data_nastere date not null,
data_deces date,
constraint pk_cod_artist primary key (cod_artist)
);


alter table ARTIST
drop column prenume_artist;

create table CURENT
(
cod_curent integer,
nume_curent varchar(30) unique,
constraint pk_cod_curent primary key (cod_curent)
);

create table CLIENTI
(
cod_client integer,
nume varchar(20) not null,
prenume varchar(20) not null,
numar_telefon varchar(25) unique,
constraint pk_cod_client primary key (cod_client)
);

create table METODA_PLATA
(
cod_met_plata integer,
metoda_plata varchar(15),
constraint pk_cod_met_plata primary key (cod_met_plata)
);

create table PICTURA
(
cod_pictura integer,
cod_artist integer,
cod_galerie integer,
cod_curent integer,
cod_bon integer,
constraint fk_coduri_artisti foreign key (cod_artist) references ARTIST(cod_artist)
ON DELETE CASCADE,
constraint fk_coduri_galerii foreign key (cod_galerie) references GALERIE(cod_galerie)
ON DELETE SET NULL,
constraint fk_coduri_curente foreign key (cod_curent) references CURENT(cod_curent)
ON DELETE CASCADE,
constraint fk_coduri_bonuri foreign key (cod_bon) references CUMPARARE(cod_bon)
ON DELETE CASCADE,
titlu varchar(50),
pret_vanzare decimal (13,2) constraint pret_vanzare_valid check (pret_vanzare>0),
constraint pk_cod_pictura primary key (cod_pictura)
);


create table CUMPARARE
(
cod_bon integer,
cod_client integer,
cod_met_plata int not null,
constraint fk_cod_client foreign key (cod_client) references CLIENTI(cod_client)
ON DELETE SET NULL, 
constraint fk_met_plata foreign key (cod_met_plata) references METODA_PLATA(cod_met_plata),
pret_cumparare decimal (13,2) constraint pret_cumparare_valid check (pret_cumparare>0),
data_cumparare date not null,
constraint pk_cod_bon primary key (cod_bon)
);





insert into ARTIST
values(100,'Vincent Van Gogh','Tarile de Jos',str_to_date('30-03-1853','%d-%m-%Y'),str_to_date('29-07-1890','%d-%m-%Y'));
insert into ARTIST
values(101,'Pablo Picasso','Spania',str_to_date('25-10-1881','%d-%m-%Y'),str_to_date('08-04-1973','%d-%m-%Y'));
insert into ARTIST
values(102,'Leonardo da Vinci','Italia',str_to_date('15-04-1452','%d-%m-%Y'),str_to_date('02-05-1519','%d-%m-%Y'));
insert into ARTIST
values(103,'Claude Monet','Franta',str_to_date('14-11-1840','%d-%m-%Y'),str_to_date('05-12-1926','%d-%m-%Y'));
insert into ARTIST
values(104,'Rembrandt Harmenszoon van Rijn','Tarile de Jos',str_to_date('15-07-1606','%d-%m-%Y'),str_to_date('04-10-1669','%d-%m-%Y'));
insert into ARTIST
values(105,'Michelangelo Merisi','Italia',str_to_date('29-09-1571','%d-%m-%Y'),str_to_date('18-07-1610','%d-%m-%Y'));
insert into ARTIST
values(106,'Frederic Leighton','Regatul Unit',str_to_date('03-12-1830','%d-%m-%Y'),str_to_date('25-01-1896','%d-%m-%Y'));
insert into ARTIST
values(107,'Peter Paul Rubens','Tarile de Jos',str_to_date('28-06-1577','%d-%m-%Y'),str_to_date('30-05-1640','%d-%m-%Y'));
metoda_platapicturainsert into ARTIST
values(108,'Gustav Klimt','Austria',str_to_date('14-07-1862','%d-%m-%Y'),str_to_date('06-02-1918','%d-%m-%Y'));
insert into ARTIST
values(109,'Edvard Muncht','Norvegia',str_to_date('12-12-1863','%d-%m-%Y'),str_to_date('23-01-1944','%d-%m-%Y'));
insert into ARTIST
values(110,'Jackson Pollock','Statele Unite ale Americii',str_to_date('28-01-1912','%d-%m-%Y'),str_to_date('11-08-1956','%d-%m-%Y'));
insert into ARTIST
values(111,'Aubrey Beardsley','Regatul Unit',str_to_date('21-08-1872','%d-%m-%Y'),str_to_date('16-03-1898','%d-%m-%Y'));
insert into ARTIST
values(112,'Piet Mondrian','Tarile de Jos',str_to_date('07-03-1872','%d-%m-%Y'),str_to_date('01-02-1944','%d-%m-%Y'));
insert into ARTIST
values(113,'David Hammons','Statele Unite ale Americii',str_to_date('24-07-1943','%d-%m-%Y'),NULL);
insert into ARTIST
values(114,'Alison Van Pelt','Statele Unite ale Americii',str_to_date('16-09-196metoda_plata3','%d-%m-%Y'),NULL);
insert into ARTIST
values(115,'Kurt Schwitters','Germania',str_to_date('20-06-1887','%d-%m-%Y'),str_to_date('08-01-1948','%d-%m-%Y'));
insert into ARTIST
values(116,'Sandro Botticelli','Franta',str_to_date('01-03-1445','%d-%m-%Y'),str_to_date('17-05-1510','%d-%m-%Y'));
insert into ARTIST
values(117,'Leon Dabo','Statele Unite ale Americii',str_to_date('09-07-1865','%d-%m-%Y'),str_to_date('07-11-1960','%d-%m-%Y'));
insert into ARTIST
values(118,'Andy Warhol','Statele Unite ale Americii',str_to_date('06-08-1928','%d-%m-%Y'),str_to_date('22-02-1987','%d-%m-%Y'));
insert into ARTIST
values(119,'Georges Seurat','Franta',str_to_date('02-12-1859','%d-%m-%Y'),str_to_date('29-03-1891','%d-%m-%Y'));
insert into ARTIST
values(120,'Jacques-Louis David','Franta',str_to_date('30-08-1748','%d-%m-%Y'),str_to_date('29-12-1825','%d-%m-%Y'));
insert into ARTIST
values(121,'Mikhail Fyodorovich Larionov','Rusia',str_to_date('03-06-1881','%d-%m-%Y'),str_to_date('10-05-1964','%d-%m-%Y'));
insert into ARTIST
values(122,'Francisco de Goya','Spania',str_to_date('30-03-1746','%d-%m-%Y'),str_to_date('16-04-1828','%d-%m-%Y'));
insert into ARTIST
values(123,'Willem de Kooning','Statele Unite ale Americii',str_to_date('24-04-1904','%d-%m-%Y'),str_to_date('19-03-1997','%d-%m-%Y'));
insert into ARTIST
values(124,'René Magritte','Belgia',str_to_date('21-11-1898','%d-%m-%Y'),str_to_date('15-08-1967','%d-%m-%Y'));
insert into ARTIST
values(125,'Edward Hopper','Statele Unite ale Americii',str_to_date('22-07-1882','%d-%m-%Y'),str_to_date('15-05-1967','%d-%m-%Y'));
insert into ARTIST
values(126,'John Cage','Statele Unite ale Americii',str_to_date('05-09-1912','%d-%m-%Y'),str_to_date('12-08-1992','%d-%m-%Y'));
insert into ARTIST
values(127,'Grant DeVolson Wood','Statele Unite ale Americii',str_to_date('13-02-1897','%d-%m-%Y'),str_to_date('12-02-1942','%d-%m-%Y'));
insert into ARTIST
values(128,'Paul Gauguin','Franta',str_to_date('07-06-1848','%d-%m-%Y'),str_to_date('09-05-1903','%d-%m-%Y'));
insert into ARTIST
values(129,'Marcel Duchamp','Franta',str_to_date('28-07-1887','%d-%m-%Y'),str_to_date('02-10-1968','%d-%m-%Y'));
insert into ARTIST
values(130,'Diego Rivera','Mexic',str_to_date('08-12-1886','%d-%m-%Y'),str_to_date('24-11-1957','%d-%m-%Y'));
insert into ARTIST
values(131,'Michelangelo Buonarroti','Italia',str_to_date('06-03-1475','%d-%m-%Y'),str_to_date('18-02-1564','%d-%m-%Y'));
insert into ARTIST
values(132,'Yves Klein','Franta',str_to_date('28-04-1928','%d-%m-%Y'),str_to_date('06-06-1962','%d-%m-%Y'));
insert into ARTIST
values(133,'Georges Braque','Franta',str_to_date('13-05-1882','%d-%m-%Y'),str_to_date('31-08-1963','%d-%m-%Y'));
insert into ARTIST
values(134,'Thomas Eakins','Franta',str_to_date('25-07-1844','%d-%m-%Y'),str_to_date('25-06-1916','%d-%m-%Y'));
insert into ARTIST
values(135,'Henri Matisse','Franta',str_to_date('31-12-1869','%d-%m-%Y'),str_to_date('03-11-1954','%d-%m-%Y'));
insert into ARTIST
values(136,'Pierre Bonnard','Franta',str_to_date('03-10-1867','%d-%m-%Y'),str_to_date('23-01-1947','%d-%m-%Y'));
insert into ARTIST
values(137,'Ferdinand Georg Waldmüller','Austria',str_to_date('15-01-1793','%d-%m-%Y'),str_to_date('23-08-1865','%d-%m-%Y'));
insert into ARTIST
values(138,'Paul Signac','Franta',str_to_date('11-11-1863','%d-%m-%Y'),str_to_date('15-08-1935','%d-%m-%Y'));
insert into ARTIST
values(139,'Edward Hicks','Statele Unite ale Americii',str_to_date('04-04-1780','%d-%m-%Y'),str_to_date('23-08-1849','%d-%m-%Y'));






insert into GALERIE
values(300,'Muzeul Luvru','+330140205104');
insert into GALERIE
values(301,'Muzeul de Arta Moderna','+3302127089400');
insert into GALERIE
values(302,'Muzeul Hermitage',' +78127109079');
insert into GALERIE
values(303,'Muzeul Tate Modern','+4402078878888');
insert into GALERIE
values(304,'Muzeul Metropolitan de Arta','+4402125357710');



insert into CLIENTI
values(400,'López','José','+34562758645');
insert into CLIENTI
values(401,'Rodríguez','Luisa','+34823465855');
insert into CLIENTI
values(402,'Ortiz','Pedro','+34777544176');
insert into CLIENTI
values(403,'Gonzales','Ricardo','+34765411203');
insert into CLIENTI
values(404,'Moreno','Bianca','+34462537757');
insert into CLIENTI
values(405,'Delgado','Fernando','+34428325435');
insert into CLIENTI
values(406,'Flores','Rodrigo','+34021350758');
insert into CLIENTI
values(407,'Salazar','Marisol','+34046340478');
insert into CLIENTI
values(408,'Medina','Manuel','+34435426857');
insert into CLIENTI
values(409,'Romero','Miranda','+34221736522');

insert into CLIENTI
values(410,'Barrere','Marie','0690548863');
insert into CLIENTI
values(411,'Bernard','Romain','0694453522');
insert into CLIENTI
values(412,'Carrel','Theo','0692425433');
insert into CLIENTI
values(413,'Descamps','Mélanie','0693238045');
insert into CLIENTI
values(414,'Gagne','Pierre','0690412314');
insert into CLIENTI
values(415,'Gagneux','Charlotte','0692075220');
insert into CLIENTI
values(416,'Cour','Arthur','0690327896');
insert into CLIENTI
values(417,'Lefebvre','Florian','0694564290');
insert into CLIENTI
values(418,'Lafitte','Juliette','0690204979');
insert into CLIENTI
values(419,'Lenoir','Marine','0693403245');

insert into CLIENTI
values(420,'Smith','James','+15417543010');
insert into CLIENTI
values(421,'Johnson','Michael','+12642647362');
insert into CLIENTI
values(422,'Miller','Maria','+14413526998');
insert into CLIENTI
values(423,'Martinez','David','+13457562474');
insert into CLIENTI
values(424,'Wilson','Robert','+18095623745');
insert into CLIENTI
values(425,'Martin','Mary','+14735835235113');
insert into CLIENTI
values(426,'Thompson','Katherine','+17672456235893');
insert into CLIENTI
values(427,'White','Jessica','+15416294004232');
insert into CLIENTI
values(428,'Brown','Lola','+18294125934');
insert into CLIENTI
values(429,'Louis','Sam','+17674825724215');

insert into CLIENTI
values(430,'Schmidt','Maximilian','+491595558525');
insert into CLIENTI
values(431,'Schneider','Noah','+491625556257');
insert into CLIENTI
values(432,'Wagner','Sofia','+491575558240');
insert into CLIENTI
values(433,'Neumann','Hanna','+491605555606');
insert into CLIENTI
values(434,'Schwarz','Liam','+491625556089');
insert into CLIENTI
values(435,'Hoffman','Mila','+491595559437');
insert into CLIENTI
values(436,'Werner','Jacob','+491725555809');
insert into CLIENTI
values(437,'Krause','Lina','+491745559167');
insert into CLIENTI
values(438,'Meier','Mia','+491605559387');
insert into CLIENTI
values(439,'Hermann','Anton','+491595556324');

insert into METODA_PLATA
values(0,'cash');
insert into METODA_PLATA
values(1,'card');
insert into METODA_PLATA
values(2,'transfer bancar');
insert into METODA_PLATA
values(3,'rata');



insert into CURENT
values(200,'Postimpresionism');
insert into CURENT
values(201,'Cubism');
insert into CURENT
values(202,'Renastere');
insert into CURENT
values(203,'Impresionsim');
insert into CURENT
values(204,'Epoca de Aur a Olandei');
insert into CURENT
values(205,'Baroc');
insert into CURENT
values(206,'Academism');
insert into CURENT
values(207,'Baroc Flamand');
insert into CURENT
values(208,'Simbolism'); 
insert into CURENT
values(209,'Expresionism'); 
insert into CURENT
values(210,'Expresionism abstract');
insert into CURENT
values(211,'Estetism');
insert into CURENT
values(212,'De Stijl');
insert into CURENT
values(213,'Postmodernism');
insert into CURENT
values(214,'Hiperrealism');
insert into CURENT
values(215,'Dadaism');
insert into CURENT
values(216,'Renasterea veche');
insert into CURENT
values(217,'Tonalism');
insert into CURENT
values(218,'Pop Art');
insert into CURENT
values(219,'Neoimpresionism');
insert into CURENT
values(220,'Neoclasicism');
insert into CURENT
values(221,'Suprematism');
insert into CURENT
values(222,'Romantism');
insert into CURENT
values(223,'Abstractia gestuala');
insert into CURENT
values(224,'Suprarealism');
insert into CURENT
values(225,'Neorealism');
insert into CURENT
values(226,'Fluxus');
insert into CURENT
values(227,'Regionalism');
insert into CURENT
values(228,'Primitivism');
insert into CURENT
values(229,'Arta Conceptuala');
insert into CURENT
values(230,'Muralism Mexican');
insert into CURENT
values(231,'Inalta Renastere');
insert into CURENT
values(232,'Cinetism');
insert into CURENT
values(233,'Fauvism');
insert into CURENT
values(234,'Realism');
insert into CURENT
values(235,'Divizionism');
insert into CURENT
values(236,'Les Nabis');
insert into CURENT
values(237,'Biedermeier');
insert into CURENT
values(238,'Pointilism');
insert into CURENT
values(239,'Arta naiva');








insert into PICTURA
values(500,100,302,200,1400,'The Starry Night',1450000000);
insert into PICTURA
values(501,101,300,201,1400,'Guernica',110000000);
insert into PICTURA
values(502,102,304,202,NULL,'Mona Lisa',2670000000);
insert into PICTURA
values(503,103,300,203,NULL,'La Promenade',6500000);
insert into PICTURA
values(504,104,301,204,NULL,'The Night Watch',110000);
insert into PICTURA
values(505,105,303,205,NULL,'Supper at Emmaus',40000);
insert into PICTURA
values(506,106,300,206,NULL,'Lachrymae',50000);
insert into PICTURA
values(507,107,300,207,1405,'The Elevation of the Cross',650000);
insert into PICTURA
values(508,108,303,208,NULL,'The Kiss',800000);
insert into PICTURA
values(509,109,304,209,NULL,'Anxiety',770000);
insert into PICTURA
values(510,110,300,210,NULL,'Autumn Rhythm',860000);
insert into PICTURA
values(511,111,303,211,NULL,'The Peacock Skirt',700000);
insert into PICTURA
values(512,112,304,212,NULL,'Gray Tree',425000);
insert into PICTURA
values(513,113,302,213,1409,'Too Onvious',225000);
insert into PICTURA
values(514,114,301,214,1409,'Silver Horse',97000);
insert into PICTURA
values(515,115,300,215,1414,'Relief in relief',200000);
insert into PICTURA
values(516,116,300,216,1436,'The Birth of Venus',310000);
insert into PICTURA
values(517,117,301,217,1432,'The Seashore',400000);
insert into PICTURA
values(518,118,304,218,NULL,'Triple Elvis',550000);
insert into PICTURA
values(519,119,302,219,1418,'Circus Sideshow',120000);
insert into PICTURA
values(520,120,300,220,1403,'The Death of Marat',340000);
insert into PICTURA
values(521,121,303,221,1419,'Soldier on a Horse',120000);
insert into PICTURA
values(522,122,304,222,1400,'Saturno devorando a su hijo',130000);
insert into PICTURA
values(523,123,300,223,1428,'Woman I',170000);
insert into PICTURA
values(524,124,302,224,1402,'The Lovers',367000);
insert into PICTURA
values(525,125,301,225,1408,'Chop Suey',401000);
insert into PICTURA
values(526,126,300,226,1411,'The Missing Stone',18150);
insert into PICTURA
values(527,127,300,227,1429,'Daughters of Revolution',10850);
insert into PICTURA
values(528,128,304,228,1411,'The Yellow Christ',104560);
insert into PICTURA
values(529,129,300,229,1437,'Duchamp',234000);
insert into PICTURA
values(530,130,300,230,1433,'The Flower Carrier',500150);
insert into PICTURA
values(531,131,304,231,1434,'David',595000);
insert into PICTURA
values(532,132,301,232,1431,'Blue Monochrome',161045);
insert into PICTURA
values(533,133,300,233,1406,'Bottle and Fishes',120170);
insert into PICTURA
values(534,134,304,234,1404,'The Agnew Clinic',90900);
insert into PICTURA
values(535,135,303,235,1406,'The Snail',89500);
insert into PICTURA
values(536,136,301,236,1425,'The Bowl of Milk',100455);
insert into PICTURA
values(537,137,302,237,1413,'Time of roses',79900);
insert into PICTURA
values(538,138,304,238,NULL,'Women at the Well',86900);
insert into PICTURA
values(539,139,301,239,1424,'Peaceable Kingdom',78500);

insert into PICTURA
values(540,100,301,200,1427,'The Potato Eaters',89000000);
insert into PICTURA
values(541,100,303,200,NULL,'The Yellow House',78900000);
insert into PICTURA
values(542,101,304,201,NULL,'The Weeping Woman',110000000);
insert into PICTURA
values(543,102,300,202,NULL,'The Last Supper',23300000);
insert into PICTURA
values(544,102,302,202,NULL,'Salvator Mundi',450000000);
insert into PICTURA
values(545,103,300,203,1401,'Impression, soleil levant',32000000);
insert into PICTURA
values(546,104,301,204,NULL,'The Jewish Bride',450000);
insert into PICTURA
values(547,104,304,204,1426,'Hundrer Guilder Print',78000);
insert into PICTURA
values(548,105,303,205,1423,'The Cardsharps',3201500);
insert into PICTURA
values(549,105,300,205,1412,'Bacchus',12150000);
insert into PICTURA
values(550,106,301,206,1401,'The Bath of Psyche',870150);
insert into PICTURA
values(551,106,302,206,NULL,'Cymon and Iphigenia',782000);
insert into PICTURA
values(552,107,302,207,1439,'Samson and Delilah',450780);
insert into PICTURA
values(553,108,301,208,NULL,'Judith and Holofernes',650126);
insert into PICTURA
values(554,109,304,209,NULL,'The Dance of Life',130530);
insert into PICTURA
values(555,109,304,209,NULL,'Vampire',230000);
insert into PICTURA
values(556,110,304,210,NULL,'Blue Poles',110560);
insert into PICTURA
values(557,112,302,212,1438,'Broadway Boogie-Woogie',98560);
insert into PICTURA
values(558,112,303,212,NULL,'Tableau I',114520);
insert into PICTURA
values(559,112,301,212,NULL,'Victory Boogie Woogie',235000);
insert into PICTURA
values(560,116,302,216,1406,'Portrait of a Young Woman',980150);
insert into PICTURA
values(561,116,301,216,NULL,'Madonna of the Book',689000);
insert into PICTURA
values(562,120,300,220,1418,'The death of Socrates',1100000);
insert into PICTURA
values(563,120,300,220,NULL,'The Intervention of the Sabine Women',230560);
insert into PICTURA
values(564,121,301,221,1415,'Dancing Soldiers',785000);
insert into PICTURA
values(565,122,302,222,1418,'The Sleep of Reason Produces Monsters',210500);
insert into PICTURA
values(566,125,304,225,NULL,'Nighthawks',98150);
insert into PICTURA
values(567,127,303,227,1420,'American Gothic',110150);
insert into PICTURA
values(568,127,302,227,1407,'Spring in Town',300000);
insert into PICTURA
values(569,128,304,228,1430,'Ave Maria',575000);
insert into PICTURA
values(570,128,304,228,1405,'By the Sea',365000);
insert into PICTURA
values(571,130,300,230,1401,'Pan American Unity',89450);
insert into PICTURA
values(572,130,303,230,1415,'Agrarian Leader Zapata',235150);
insert into PICTURA
values(573,131,302,231,NULL,'Moses',1500000);
insert into PICTURA
values(574,131,301,231,1435,'Pieta',985000);
insert into PICTURA
values(575,131,301,231,NULL,'Deposition',205000);
insert into PICTURA
values(576,132,302,232,1417,'Fire Painting',565150);
insert into PICTURA
values(577,132,300,232,1422,'Blue Venus',320120);
insert into PICTURA
values(578,133,300,233,1410,'Fruit Dish and Glass',540150);
insert into PICTURA
values(579,133,304,233,NULL,'Glass on a Table',460000);
insert into PICTURA
values(580,134,304,234,1411,'Arcadia',256900);
insert into PICTURA
values(581,136,302,236,1402,'The Garden Steps',390400);
insert into PICTURA
values(582,136,303,236,1401,'Dining Room on the Garden',623150);
insert into PICTURA
values(583,137,300,237,1421,'The Birthday Table',452500);
insert into PICTURA
values(584,138,301,238,1416,'Port of La Rochelle',670400);



insert into CUMPARARE
values('1400',400,3,3866045000,str_to_date('12-05-2018','%d-%m-%Y'));
insert into CUMPARARE
values('1401',401,2,67738300,str_to_date('17-04-2017','%d-%m-%Y'));
insert into CUMPARARE
values('1402',402,1,1347400,str_to_date('30-03-2019','%d-%m-%Y'));
insert into CUMPARARE
values('1403',403,1,740000,str_to_date('02-04-2020','%d-%m-%Y'));
insert into CUMPARARE
values('1404',404,1,170900,str_to_date('06-12-2015','%d-%m-%Y'));
insert into CUMPARARE
values('1405',405,0,10775000,str_to_date('14-01-2013','%d-%m-%Y'));
insert into CUMPARARE
values('1406',406,2,1974820,str_to_date('02-01-2020','%d-%m-%Y'));
insert into CUMPARARE
values('1407',407,1,980000,str_to_date('19-12-2019','%d-%m-%Y'));
insert into CUMPARARE
values('1408',408,3,507000,str_to_date('04-08-2012','%d-%m-%Y'));
insert into CUMPARARE
values('1409',409,2,674000,str_to_date('25-05-2017','%d-%m-%Y'));
insert into CUMPARARE
values('1410',410,2,899150,str_to_date('14-12-2018','%d-%m-%Y'));
insert into CUMPARARE
values('1411',411,2,778610,str_to_date('23-10-2017','%d-%m-%Y'));
insert into CUMPARARE
values('1412',412,1,25350000,str_to_date('11-09-2016','%d-%m-%Y'));
insert into CUMPARARE
values('1413',413,0,152900,str_to_date('17-07-2019','%d-%m-%Y'));
insert into CUMPARARE
values('1414',414,3,900000,str_to_date('19-04-2009','%d-%m-%Y'));
insert into CUMPARARE
values('1415',415,3,1981150,str_to_date('20-03-2019','%d-%m-%Y'));
insert into CUMPARARE
values('1416',416,2,890400,str_to_date('21-07-2017','%d-%m-%Y'));
insert into CUMPARARE
values('1417',417,2,1200150,str_to_date('08-07-2015','%d-%m-%Y'));
insert into CUMPARARE
values('1418',418,2,2015500,str_to_date('21-01-2014','%d-%m-%Y'));
insert into CUMPARARE
values('1419',419,1,1355000,str_to_date('11-11-2010','%d-%m-%Y'));
insert into CUMPARARE
values('1420',420,0,10915150,str_to_date('01-10-2017','%d-%m-%Y'));
insert into CUMPARARE
values('1421',421,0,985500,str_to_date('08-01-2020','%d-%m-%Y'));
insert into CUMPARARE
values('1422',422,3,785120,str_to_date('24-12-2019','%d-%m-%Y'));
insert into CUMPARARE
values('1423',423,3,382770060,str_to_date('28-11-2018','%d-%m-%Y'));
insert into CUMPARARE
values('1424',424,1,150500,str_to_date('11-04-2016','%d-%m-%Y'));
insert into CUMPARARE
values('1425',425,2,270455,str_to_date('01-04-2017','%d-%m-%Y'));
insert into CUMPARARE
values('1426',426,0,155000,str_to_date('07-06-2017','%d-%m-%Y'));
insert into CUMPARARE
values('1427',427,3,268000000,str_to_date('06-03-2012','%d-%m-%Y'));
insert into CUMPARARE
values('1428',428,3,2370000,str_to_date('14-11-2011','%d-%m-%Y'));
insert into CUMPARARE
values('1429',429,0,59850,str_to_date('03-02-2009','%d-%m-%Y'));
insert into CUMPARARE
values('1430',430,1,874000,str_to_date('05-07-2017','%d-%m-%Y'));
insert into CUMPARARE
values('1431',431,3,1739046,str_to_date('25-05-2011','%d-%m-%Y'));
insert into CUMPARARE
values('1432',432,2,900000,str_to_date('17-04-2008','%d-%m-%Y'));
insert into CUMPARARE
values('1433',433,2,855150,str_to_date('23-08-2009','%d-%m-%Y'));
insert into CUMPARARE
values('1434',434,3,47038560,str_to_date('11-09-2018','%d-%m-%Y'));
insert into CUMPARARE
values('1435',435,2,1785000,str_to_date('13-04-2010','%d-%m-%Y'));
insert into CUMPARARE
values('1436',436,1,974000,str_to_date('14-04-2017','%d-%m-%Y'));
insert into CUMPARARE
values('1437',437,2,1034000,str_to_date('30-11-2014','%d-%m-%Y'));
insert into CUMPARARE
values('1438',438,3,201560,str_to_date('24-11-2012','%d-%m-%Y'));
insert into CUMPARARE
values('1439',439,0,1808780,str_to_date('15-01-2009','%d-%m-%Y'));





--DELETE from CLIENTI WHERE cod_client=440

