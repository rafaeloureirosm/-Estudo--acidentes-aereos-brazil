'''
This dataset was translated to English in order to help you to create analysis about its data. 
Be free to share and modify this script to achieve new goals.
   
My e-mail: paulovasconcellos@iestampa.com.br
My blog (Brazilian Portuguese): https://paulovasconcellos.com.br
'''

import pandas as pd

aircrafts = pd.read_csv('../dataset/aeronaves.csv', parse_dates=['dia_extracao', 'ano_fabricacao'])

#translating column names
aircrafts.columns = ['aircraft_id', 'occurrence_id', 'registration', 'operator_id', 'equipment', 'manufacturer',
                    'model', 'engine_type', 'engines_amount', 'takeoff_max_weight (Lbs)', 'seatings_amount', 'year_manufacture',
                    'registration_country', 'registration_category', 'registration_aviation', 'origin_flight', 
                    'destination_flight', 'operation_phase', 'type_operation', 'damage_level', 'fatalities_amount',
                    'extraction_day']

#equipment translation
aircrafts['equipment'] = aircrafts['equipment'].map({'AVIÃO': 'AIRPLANE',
                                                   'HELICÓPTERO': 'HELICOPTER',
                                                   'PLANADOR': 'GLIDER',
                                                   'ULTRALEVE': 'ULTRALIGHT',
                                                   'ANFÍBIO': 'AMPHIBIOUS',
                                                   '***': 'UNKNOWN',
                                                   'DIRIGÍVEL': 'AIRSHIP'})

#engine type translation
aircrafts['engine_type'] = aircrafts['engine_type'].map({'PISTÃO': 'PISTON',
                                                       'JATO': 'JET',
                                                       'TURBOEIXO': 'TURBOSHAFT',
                                                       'TURBOÉLICE': 'TURBOPROP',
                                                       'SEM TRAÇÃO': 'WITHOUT TRACTION',
                                                       '***': 'UNKNOWN'})

#converting kg to lbs
aircrafts['takeoff_max_weight (Lbs)'] = (aircrafts['takeoff_max_weight (Lbs)'] * 2.20462).astype(int)

#country's name translation
aircrafts['registration_country'] = aircrafts['registration_country'].map({'BRASIL': 'BRAZIL',
                                      'ESTADOS UNIDOS': 'USA',
                                      'NÃO IDENTIFICADO': 'UNKNOWN',
                                      'FRANÇA': 'FRENCH',
                                      'ESPANHA': 'SPAIN',
                                      'ÁFRICA DO SUL': 'SOUTH AFRICA',
                                      'URUGUAI': 'URUGUAY',
                                      'RÚSSIA': 'RUSSIA',
                                      'POLÔNIA': 'POLAND',
                                      'ARÁBIA SAUDITA': 'SAUDI ARABIA',
                                      'ALEMANHA': 'GERMAN'
                                      })

aircrafts['registration_aviation'] = aircrafts['registration_aviation'].map({'INSTRUÇÃO': 'INSTRUCTION',
                                                                           'TÁXI AÉREO': 'AEROTAXI',
                                                                           'PARTICULAR': 'PRIVATE',
                                                                           'REGULAR': 'REGULAR',
                                                                           'ADMINISTRAÇÃO DIRETA': 'DIRECT ADMINISTRATION',
                                                                           'MÚLTIPLA': 'MULTIPLE',
                                                                           'AGRÍCOLA': 'AGRICULTURAL',
                                                                           'EXPERIMENTAL': 'EXPERIMENTAL',
                                                                           'ESPECIALIZADA': 'SPECIALIZED',
                                                                           'ADMINISTRAÇÃO INDIRETA': 'INDIRECT ADMINISTRATION',
                                                                           'NÃO REGULAR': 'NOT REGULAR',
                                                                           '***': 'UNKNOWN',
                                                                           'HISTÓRICA': 'HISTORIC'
                                                                          })

#operation phase translation
aircrafts['operation_phase'] = aircrafts['operation_phase'].map({'INDETERMINADA': 'UNKNOWN',
                                                               'DECOLAGEM': 'TAKEOFF',
                                                               'CORRIDA APÓS POUSO': 'RUN AFTER LANDING',
                                                               'SUBIDA': 'ASCENSION',
                                                               'MANOBRA': 'MANEUVER',
                                                               'PAIRADO': 'HOVERING',
                                                               'APROXIMAÇÃO FINAL': 'FINAL APPROXIMATION',
                                                               'ARREMETIDA NO SOLO': 'RUSH ON THE GROUND',
                                                               'POUSO': 'LANDING',
                                                               'DESCIDA': 'DESCEND',
                                                               'CRUZEIRO': 'CRUISE',
                                                               'CIRCUITO DE TRÁFEGO': 'TRAFFIC CIRCUIT',
                                                               'TÁXI': 'TAXI',
                                                               'ARREMETIDA NO AR': 'RUSH IN THE AIR',
                                                               'ESPECIALIZADA': 'SPECIALIZED',
                                                               'OUTRA FASE': 'ANOTHER PHASE',
                                                               'NAVEGAÇÃO A BAIXA ALTURA': 'LOW ALTITUDE NAVIGATION',
                                                               'RETA FINAL': 'FINAL STRETCH',
                                                               'PARTIDA DO MOTOR': 'ENGINE START',
                                                               'CHEQUE DE MOTOR OU ROTOR': 'ENGINE OR ROTOR CHECKING',
                                                               'DECOLAGEM VERTICAL': 'VERTICAL TAKEOFF',
                                                               'OPERAÇÃO DE SOLO': 'GROUND OPERATION',
                                                               'ESTACIONAMENTO': 'PARKING'
                                                              })

#type operation translation
aircrafts['type_operation'] = aircrafts['type_operation'].map({'INSTRUÇÃO': 'INSTRUCTION',
                                                             'TÁXI AÉREO': 'AEROTAXI',
                                                             'PRIVADA': 'PRIVATE',
                                                             'REGULAR': 'REGULAR',
                                                             'POLICIAL': 'POLICIAL',
                                                             'AGRÍCOLA': 'AGRICULTURAL',
                                                             'EXPERIMENTAL': 'EXPERIMENTAL',
                                                             'ESPECIALIZADA': 'SPECIALIZED',
                                                             'NÃO REGULAR': 'NOT REGULAR',
                                                             '***': 'UNKNOWN'
                                                            })

aircrafts['damage_level'] = aircrafts['damage_level'].map({'SUBSTANCIAL': 'SUBSTANTIAL',
                                                         'LEVE': 'LIGHT',
                                                         'NENHUM': 'NONE',
                                                         '***': 'UNKNOWN',
                                                         'DESTRUÍDA': 'DESTROYED'
                                                        })

#creating a new csv file
aircrafts.to_csv('../dataset/aircrafts.csv')

