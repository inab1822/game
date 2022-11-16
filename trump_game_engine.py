# ===============================================트럼프 게임========================================================= 
import test_game

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


     
def trump_game_step2(game_name):
    try:
        nick_name = input('닉네임을 입력하세요. 단, 20자 이내로')
        if len(nick_name) > 20:
            raise Exception('초과되었습니다. 다시 입력해주세요')
    except Exception as e:
        print(e)
        trump_game_step2()
    else:
        print_game_name = ' ' * ((len('='*48) - wcswidth('✨🎉'+game_name+'🎉✨')) // 2)
        print_nick_name =  ' ' * ((len('='*48) - wcswidth('welcome'+ nick_name)) // 2)
        print('=' * 50)
        print(f'={print_game_name}✨🎉{game_name}🎉✨{print_game_name}=')
        print(f'={print_nick_name}welcome {nick_name}{print_nick_name}=')
        print('='*50)
        trump_game_step3(nick_name) # 이부분 가운데로 출력하기
        
def trump_game_step3(nick_name):
    trump_game_start_answer = input(f'환영합니다!!{nick_name}님 게임을 시작하시겠습니까?')
    if trump_game_start_answer == 'yes':
        trump_game_step4(nick_name)
    elif trump_game_start_answer == 'no':
        print('처음으로 돌아갑니다.')
        test_game.game_step1()
    else:
        print('옳바르지 않은 입력입니다. 다시 입력해주세요')
        trump_game_step3()

def trump_game_step4(nick_name):
    card_num = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
    card_pattern = list('♠◆♥♣')
    print(card_num)
    print(card_pattern)

    card = list()
    for num in card_num:
        for pattern in reversed(card_pattern):
            card.append(pattern+num)
    print('카드가 섞였습니다')
    remix = input('다시 섞으시겠습니까?')
    if remix == 'yes':
        trump_game_step4(nick_name)
    elif remix == 'no':
        print('게임을 시작합니다')
        trump_game_step5(nick_name)
    else:
        print('옳바르지 않은 입력입니다. 다시 입력해주세요')
        trump_game_step4(nick_name)       
        
def trump_game_step5(nick_name):
    card_num = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
    card_pattern = list('♠◆♥♣')
    print(card_num)
    print(card_pattern)

    card = list()
    for num in card_num:
        for pattern in reversed(card_pattern):
            card.append(pattern+num)
    
    
    computer_score = 0
    player_score = 0
    for i in range(10):
        game_deck = card.copy()
        computer_deck = game_deck.pop(random.randint(0,51))
        player_deck = game_deck.pop(random.randint(0,51))
        if card.index(computer_deck) > card.index(player_deck):
            computer_score += 10
            print(f'컴퓨터의 카드는{computer_deck}!!')
            print(f'{nick_name}님의 카드는{player_deck}!!')
            print(f'승자는 컴퓨터입니다!')
        elif card.index(computer_deck) < card.index(player_deck):
            player_score += 10
            print(f'컴퓨터의 카드는{computer_deck}!!')
            print(f'{nick_name}님의 카드는{player_deck}!!')
            print(f'승자는 {nick_name}님 입니다!')
        else:
            computer_score += 5
            player_score += 5
    if computer_score > player_score:
        print(f'총 스코어 {computer_score} 대 {player_score}로 컴퓨터의 승리입니다.')
        trump_game_step6(nick_name)
    elif computer_score < player_score:
        print(f'총 스코어 {computer_score} 대 {player_score}로 {nick_name}님의 승리입니다.')
        print(f'축하드립니다!!!{nick_name}님!')
        trump_game_step6(nick_name)


def trump_game_step6(nick_name):
    start_again_answer = input('다시 하시겠습니까?')
    if start_again_answer == 'yes':
       trump_game_step4(nick_name)
    elif start_again_answer == 'no':
        print('Good Bye~')
    else:
        print('옳바른 입력이 아닙니다')
        trump_game_step4(nick_name)       