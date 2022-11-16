# =====================================업앤다운 게임====================================================================
from wcwidth import wcswidth
import random

class Error(Exception):
  '''에러입니다'''
  pass

class ValueTooSmallError(Error):
  '''너무 작은 값을 받았을 때 발생하는 에러입니다'''
  pass
class VallueTooLargeError(Error):
  '''너무 큰 값을 받았을 때 발생하는 에러입니다.'''
  pass



def number_game_step2(game_name):
    try:
        nick_name = input('닉네임을 입력하세요. 단, 20자 이내로')
        if len(nick_name) > 20:
            raise Exception('초과되었습니다. 다시 입력해주세요')
    except Exception as e:
        print(e)
        number_game_step2()
    else:
        print_game_name = ' ' * ((len('='*48) - wcswidth('✨🎉'+game_name+'🎉✨')) // 2)
        print_nick_name =  ' ' * ((len('='*48) - wcswidth('welcome'+ nick_name)) // 2)
        print('=' * 50)
        print(f'={print_game_name}✨🎉{game_name}🎉✨{print_game_name}=')
        print(f'={print_nick_name}welcome {nick_name}{print_nick_name}=')
        print('='*50)
        number_game_step3() # 이부분 가운데로 출력하기
        

def number_game_step3():
    import random
    ran_number = random.randint(1,100)
    score = 100
    count = 0
    while True:
        try:
            your_number = int(input('1 ~ 100 까지 입력하세요'))
            if not your_number or type(your_number) == str:
                raise Exception('숫자를 입력해주세요')
            elif your_number > ran_number:
                score -= 10
                count += 1
                raise VallueTooLargeError
            elif your_number < ran_number:
                score -= 10
                count += 1
                raise ValueTooSmallError
            break
        except VallueTooLargeError:
            print('입력한 숫자보다 작습니다.')
        except ValueTooSmallError:
            print('입력한 숫자보다 큽니다.')
            
    print(f'정답입니다. 총{count}회 시도해서 {score}점 얻으셨습니다')
    number_game_step4()
    
            
def number_game_step4():
    start_again_answer = input('다시 하시겠습니까?')
    if start_again_answer == 'yes':
        number_game_step3()
    elif start_again_answer == 'no':
        print('Good Bye~')
    else:
        print('옳바른 입력이 아닙니다')
        number_game_step4()
        
   
# ====================================================업엔다운게임=================================================== 