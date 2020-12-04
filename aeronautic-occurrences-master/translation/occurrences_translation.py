'''
This dataset was translated to English in order to help you to create analysis about its data. 
Be free to share and modify this script to achieve new goals.
   
My e-mail: paulovasconcellos@iestampa.com.br
My blog (Brazilian Portuguese): https://paulovasconcellos.com.br
'''

#importing libraries
import pandas as pd

#reading file
occurrences = pd.read_csv('../dataset/occurrences.csv', parse_dates=['dia_ocorrencia', 'dia_publicacao', 'dia_extracao'])

#renaming columns
occurrences.columns = ['occurrence_id','classification','type of occurrence','localization','fu','country','aerodrome',
                       'occurrence_day','time','under_investigation','investigating_command','investigation_status',
                       'report_number','published_report','publication_day','recommendation_amount','aircrafts_involved',
                       'takeoff','extraction_day']


#translating occurrences classification
occurrences['classification'] = occurrences['classification'].map({'ACIDENTE': 'ACCIDENT',
                                                                   'INCIDENTE GRAVE': 'SERIOUS INCIDENT'})

#translating type of occurrences to English
occurrences['type of occurrence'] = occurrences['type of occurrence'].map({'FALHA DO MOTOR EM VOO': 'ENGINE FAILURE DURING THE FLIGHT',
                                                                           'POUSO SEM TREM': 'LANDING WITHOUT LANDING GEAR',
                                                                           'PERDA DE CONTROLE NO SOLO': 'LOSS OF CONTROL ON THE GROUND',
                                                                           'POUSO LONGO': 'SLOW LANDING',
                                                                           'PERDA DE CONTROLE EM VOO': 'LOSS OF CONTROL IN THE AIR',
                                                                           'INDETERMINADA': 'UNKNOWN',
                                                                           'COM TREM DE POUSO': 'ABOUT LANDING GEAR',
                                                                           'CFIT - COLISÃO EM VOO CONTROLADO COM O TERRENO': 'TERRAIN COLLISION',
                                                                           'INCURSÃO EM PISTA': 'TRACK INCURSION',
                                                                           'CAUSADO POR FENÔMENO METEOROLÓGICO EM VOO': 'METEOROLOGICAL PHENOMENOM IN THE AIR',
                                                                           'POUSO BRUSCO': 'HARD LANDING',
                                                                           'OUTROS TIPOS': 'ANOTHER TYPES',
                                                                           'COM ROTOR': 'ABOUT ROTOR',
                                                                           'FALHA DE SISTEMA / COMPONENTE': 'SYSTEM / COMPONENT FAILURE',
                                                                           'COLISÃO EM VOO COM OBSTÁCULO': 'COLLISION AGAINST OBSTACLE DURING THE FLIGHT',
                                                                           'COM PÁRA-BRISAS / JANELA / PORTA': 'ABOUT WINDOWS / DOORS / WINDSHIELD',
                                                                           'PERDA DE COMPONENTE EM VOO': 'LOSS OF COMPONENT DURING THE FLIGHT',
                                                                           'COLISÃO COM OBSTÁCULO NO SOLO': 'COLLISION AGAINST OBSTACLE ON THE GROUND',
                                                                           'FOGO EM VOO': 'FIRE DURING THE FLIGHT',
                                                                           'POUSO ANTES DA PISTA': 'LANDING BEFORE THE TRACK AREA',
                                                                           'COM LANÇAMENTO DE CARGA': 'LOAD LAUNCH',
                                                                           'DESCOMPRESSÃO NÃO INTENCIONAL /  EXPLOSIVA': 'EXPLOSIVE / NOT INTENTIONAL DECOMPRESSION',
                                                                           'COLISÃO DE AERONAVES EM VOO': 'AIRCRAFTS COLLISION IN THE AIR',
                                                                           'DESORIENTAÇÃO ESPACIAL': 'SPATIAL UNAWARENESS',
                                                                           'POUSO EM LOCAL NÃO PREVISTO': 'LANDING ON UNPREDICTABLE PLACE',
                                                                           'ESTOURO DE PNEU': 'TIRE BURST',
                                                                           'PANE SECA': 'FUEL STARVATION',
                                                                           'PERDA DE COMPONENTE NO SOLO': 'COMPONENT LOSS ON THE GROUND',
                                                                           'COM HÉLICE': 'ABOUT PROPELLER',
                                                                           'MANOBRAS A BAIXA ALTURA': 'LOW ALTITUDE MANEUVERS',
                                                                           'FOGO NO SOLO': 'FIRE ON THE GROUND',
                                                                           'COLISÃO DE VEÍCULO COM AERONAVE': 'VEHICLE COLLISION AGAINST AIRCRAFT',
                                                                           'FOD - DANO CAUSADO POR OBJETO ESTRANHO': 'FOD - DAMAGE CAUSED BY UNKNOWN OBJECT',
                                                                           'COLISÃO EM VOO COM OBJETO REBOCADO': 'COLLISION DURING THE FLIGHT AGAINST TOWED OBJECT',
                                                                           'AERONAVE ATINGIDA POR OBJETO': 'AIRCRAFT HIT BY OBJECT',
                                                                           'CAUSADO POR FENÔMENO METEOROLÓGICO NO SOLO': 'METEOROLOGICAL PHENOMENOM ON THE GROUND',
                                                                           'COLISÃO COM AERONAVE NO SOLO': 'AIRCRAFTS COLLISION ON THE GROUND',
                                                                           'FALHA ESTRUTURAL': 'STRUCTURAL FAILURE',
                                                                           'TRÁFEGO AÉREO': 'AIR TRAFFIC',
                                                                           'COM COMANDOS DE VOO': 'FLIGHT COMMANDS',
                                                                           'VAZAMENTO DE OUTROS FLUÍDOS': 'FLUID LEAKS',
                                                                           'FUMAÇA NA CABINE': 'SMOKE IN THE CABIN',
                                                                           'SAÍDA DE PISTA': 'LEAVING THE TRACK',
                                                                           'COM PESSOAL EM VOO': 'ABOUT PASSENGERS/CREW DURING THE FLIGHT',
                                                                           'CORTE INVOLUNTÁRIO DO MOTOR': 'INVOLUNTARY ENGINE CUT OFF',
                                                                           'PROBLEMAS FISIOLÓGICOS': 'PHYSIOLOGICAL PROBLEMS',
                                                                           'COM LANÇAMENTO DE PESSOAS': 'PEOPLE LAUNCH',
                                                                           'COLISÃO COM PÁSSARO': 'COLLISION AGAINST BIRD',
                                                                           'FALHA DO MOTOR NO SOLO': 'ENGINE FAILURE IN THE GROUND'})

#translating country's name
occurrences['country'] = occurrences['country'].map({'BRASIL': 'BRAZIL',
                                                     'PARAGUAI': 'PARAGUAY',
                                                     'URUGUAI': 'URUGUAY',
                                                     'COLÔMBIA': 'COLOMBIA',
                                                     'PERU': 'PERU',
                                                     'ARGENTINA': 'ARGENTINA',
                                                     'INGLATERRA': 'ENGLAND'})

#converting dates to US date format
occurrences['occurrence_day'].apply(lambda x: x.strftime('%m/%d/%Y'))
occurrences[occurrences['publication_day'].notnull()]['publication_day'].apply(lambda x: x.strftime('%m/%d/%Y'))
occurrences[occurrences['extraction_day'].notnull()]['extraction_day'].apply(lambda x: x.strftime('%m/%d/%Y'))

#under_investigation values translation
occurrences['under_investigation'] = occurrences['under_investigation'].map({'***': 'UNKNOWN',
                                        'SIM': 'YES',
                                        'NÃO': 'NO'})

#translating investigation status
occurrences['investigation_status'] = occurrences['investigation_status'].map({'FINALIZADA': 'FINISHED',
                                                                               'ATIVA': 'IN PROGRESS',
                                                                               'REABERTA': 'REOPENED'})

#report numbers which does not have a registry will be translated as Undefined
occurrences['report_number'] = occurrences['report_number'].map({'A DEFINIR': 'UNDEFINED'})

#creating new csv file
occurrences.to_csv('../dataset/occurrences.csv')