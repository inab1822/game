import trump_game_engine, number_game_engine
# from number_game_engine import *
def game_step1():
    print('Enjoy, Custom Game World')
    game_name = input('게임 이름을 입력하세요. 단, 20자 이내로')
    try:
        if len(game_name) > 20:
            raise Exception('초과되었습니다. 다시 입력해주세요')
        elif game_name == 'number_game':
            number_game_engine.number_game_step2(game_name)
            
        elif game_name == 'trump_game':
            trump_game_engine.trump_game_step2(game_name)
    except Exception as e:
        print(e)
        game_step1()
        
        
game_step1()