import sqlite3
print('1,welcome use YI system. you can insert h for help')
print('2,you can input q for quit')
print('3, you can use the command next for diffrent YI')
print('       -- 1 for 乾')
print('       -- 2 for 坤')

conn = sqlite3.connect('test.db')

while 1:
    print('please input you code')
        code = input()
	    
	        if type(code) == type(1):
		        
			        c = conn.cursor()
				        try:
					            c.execute('select * from base where id = "%s"' % code)
						                ret = c.fetchone()
								            print('---------id------------name------------')
									                str = '---------'
											            for r in ret:
												                    str += r
														            except:
															                print('没有该卦象！')
																	        finally:
																		            c.close()
																			        else:
																				        break
																					conn.close()
																					print('------------------over---------------')
