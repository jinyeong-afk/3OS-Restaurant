from threading import Thread # 스레드 모듈
import datetime as dt
import sys
import os
import random

class money: # 돈 클래스
    def __init__(self): # 돈 초기값 설정
        self.__cashes = 0
        
    @property
    def cashes(self): # 돈 get 함수
        return self.__cashes

    @cashes.setter
    def cashes(self, v): # 돈 계산하는 set 함수
        self.__cashes += v

class employee: # 종업원 클래스
    def __init__(self): # 종업원 수 기본값 설정
        self.__employee_number = 1

    @property
    def employeenum(self): # 종업원 수 get 함수
        return self.__employee_number

    @employeenum.setter
    def employeenum(self, num): # 종업원 수 set 함수
        self.__employee_number = num

    def act_employ(self): # 종업원 고용하는 함수        
        if money.cashes() >= 1000 and employee_number < 3:
            employee_number(self.__employee_number + 1)
            money.cashes(-1000)
        else:
            print('종업원을 고용하기에 돈이 모자랍니다.')

class number: # number get set 클래
    def __init__(self):
        self.__max_num = 0
        self.__enter_num = 0
        self.__out_num = 0
        self.__food_num = 0
        self.__food_status = 0
        self.__table_index = 0
    @property
    def enter_num(self): # 들어온 손님 수 get 함수
        return self.__enter_num
    @enter_num.setter
    def enter_num(self, value): # 들어온 손님 수 set 함수
        self.__enter_num += value
    @property
    def out_num(self): # 나간 손님 수 get 함수
        return self.__out_num
    @out_num.setter
    def out_num(self, value): # 나간 손님 수 set 함수
        self.__out_num += value
    @property
    def max_num(self): # 최대 손님 수 get 함수
        return self.__max_num
    @max_num.setter
    def max_num(self, value): # 최대 손님 수 set 함수
        self.__max_num = value
    @property
    def food_num(self): # 조리한 음식 수 get 함수
        return self.__food_num
    @food_num.setter
    def food_num(self, value): # 조리한 음식 수 set 함수
        self.__food_num += value
    @property
    def food_status(self): # 음식 상태 get 함수
        return self.__food_status
    @food_status.setter
    def food_status(self, value): # 음식 상태 set 함수
        self.__food_status = value
    @property
    def table_index(self): # 테이블 idext get 함수
        return self.__table_index
    @table_index.setter
    def table_index(self, value): # 테이블 index set 함수
        self.__table_index = value
        
        
class customer: # 손님 클래스
    def __init__(self): # 초기 손님 테이블 상태 설정
        self.__ftablestatus = 0
        self.__stablestatus = 0
        self.__ttablestatus = 0
        self.__fotablestatus = 0
    @property
    def ftablestatus(self): # 테이블 상태 get 함수
        return self.__ftablestatus
    @ftablestatus.setter
    def ftablestatus(self, value): # 테이블 상태 set 함수
        self.__ftablestatus = value

    @property
    def stablestatus(self): # 테이블 상태 get 함수
        return self.__stablestatus
    @stablestatus.setter
    def stablestatus(self, value): # 테이블 상태 set 함수
        self.__stablestatus = value

    @property
    def ttablestatus(self): # 테이블 상태 get 함수
        return self.__ttablestatus
    @ttablestatus.setter
    def ttablestatus(self, value): # 테이블 상태 set 함수
        self.__ttablestatus = value

    @property
    def fotablestatus(self): # 테이블 상태 get 함수
        return self.__fotablestatus
    @fotablestatus.setter
    def fotablestatus(self, value): # 테이블 상태 set 함수
        self.__fotablestatus = value
        
    def enter_time(self): # 손님 생성
        cos_enter_time = dt.datetime.now() + dt.timedelta(seconds = random.randrange(3,5)) # 랜덤으로 5~10초
        while True:
            if dt.datetime.now() >= cos_enter_time: # 랜덤한 시간 후에 손님 입장
                break;
        print('손님이 입장하였습니다.\n')
        num.enter_num = 1


    def cus_exit(self, index_table): # 손님 아웃
        exit_time = dt.datetime.now() + dt.timedelta(seconds = random.randrange(5, 11))
        while True:
            if dt.datetime.now() >= exit_time: # 랜덤한 시간 후에 손님 나감
                if index_table == 0:
                    cos.ftablestatus = 0
                elif index_table == 1:
                    cos.stablestatus = 0
                elif index_table == 2:
                    cos.ttablestatus = 0
                elif index_table == 3:
                    cos.fotablestatus = 0
                break;
        print('손님이 나갔습니다.')
        num.out_num = 1

class food:
    def __init__(self): # 초기 조리 남은 시간 설정
        self.__cooktimer = 0
        
    @property
    def cooktimer(self): # 조리 시간 get 함수
        return self.__cooktimer
    
    @cooktimer.setter
    def cooktimer(self, time): # 조리 시간 set 함수
        self.__cooktimer = time
        
    def cook_food(self, line, start_time): # 음식을 만드는 스레드를 담당하는 함수
        cook_time = 0
        cook_time = 5 #음식을 조리할 경우 조리 시간 5초
        table_index = 0     
        finish_time = start_time + dt.timedelta(seconds=cook_time) # 현재 시간에 음식 조리시간을 더해 조리 종료 시간을 계산
        while(dt.datetime.now() <= finish_time): #음식 조리가 끝날 때까지 일정 시간마다 남은 시간 출력
            left_time = finish_time - dt.datetime.now()
            food.cooktimer = left_time.seconds # 조리 시간을 set 함수로 넘겨준다
        num.food_status = 0 # 음식 조리 상태를 off 상태로 만든다
        num.food_num = 1 # 조리한 음식 수를 1 증가시켜준다

        # 빈 테이블에 손님을 앉힌다    
        if cos.ftablestatus == 0: # 빈 테이블 확인
            cos.ftablestatus = 1 #빈 테이블에 손님을 앉힘
            table_index = 0
        elif cos.stablestatus == 0:
            cos.stablestatus = 1
            table_index = 1
        elif cos.ttablestatus == 0:
            cos.ttablestatus = 1
            table_index = 2
        elif cos.fotablestatus == 0:
            cos.fotablestatus = 1
            table_index = 3
        
        cus_exit = Thread(target = cos.cus_exit, args=[table_index]) # 손님 아웃 스레드 생성
        cus_exit.start() # 손님 아웃 스레드 시작

class prints:
              
    def print_money(self): # 돈을 출력해주는 함수
        
        get_money = m.cashes

        print('돈: %d원 ' % m.cashes)

    def print_cooktime(self): # 조리 시간을 출력해주는 함수
        
        get_cooktime = coo.cooktimer
        if get_cooktime >= 60:
            get_cooktime = 0
        print('조리 시간: %d초' % get_cooktime)

    def print_employeenum(self): # 종업원 수 출력
        
        get_employeenum = e.employeenum
        print('종업원 수: %d명' % get_employeenum)

    def print_table(self): # 테이블 상태 출력
        
        if cos.ftablestatus == 1:  
            print('[O] ', end = '') # 손님이 있을 경우
        else:
            print('[X] ', end = '') # 손님이 없을 경우
        if cos.stablestatus == 1:
            print('[O] ', end = '')
        else:
            print('[X] ', end = '')
        if cos.ttablestatus == 1:
            print('[O] ', end = '')
        else:
            print('[X] ', end = '')
        if cos.fotablestatus == 1:
            print('[O] ', end = '')
        else:
            print('[X]')

    def all_print(self): # 모든 출력들을 출력해주는 함수
        now_time = dt.datetime.now() + dt.timedelta(seconds = 3)
        while True:
            if dt.datetime.now() >= now_time:
                os.system('cls')
                p.print_money() # 돈 출력 함수
                p.print_employeenum() # 종업원 수 출력 함수
                p.print_table() # 테이블 상태 출력 함수
                p.print_cooktime() # 조리 시간 출력 함수
                now_time = now_time + dt.timedelta(seconds = 1) # 1초마다 출력
            if num.max_num < num.out_num:
                 break;

if __name__ == "__main__":
    num = number()
    cos = customer()
    coo = food()
    m = money()
    p = prints()
    e = employee()
    add_money = 3000 # 음식 가격
    num.max_num = int(input('오늘 받을 손님 수를 입력하세요: '))
    th_cos_enter = Thread(target= cos.enter_time) # 손님 생성 스레드 초기화
    customer_first = Thread(target = coo.cook_food, args=(1, dt.datetime.now())) # 1번 라인 음식 조리 스레드 초기화
    th_cos_enter.start()
    th_print = Thread(target = p.all_print) # 출력 스레드
    th_print.start() # 출력 스레드 시작
    while(True):
        if not th_cos_enter.is_alive() and num.enter_num < num.max_num: # 손님 생성 스레드가 살아있지 않을 때
            th_cos_enter = Thread(target= cos.enter_time) # 손님 생성 스레드
            th_cos_enter.start() # 손님 생성 스레드 시작
            
        if num.enter_num > (num.food_num + num.food_status):
            if not customer_first.is_alive(): # 음식 조리 스레드가 살아있지 않을 때
                customer_first = Thread(target = coo.cook_food, args=(1,dt.datetime.now())) # 1번 라인 음식 조리 스레드
                customer_first.start() # 음식 조리 스레드 시작
                num.food_status = 1

                m.cashes = add_money # 음식 값 더하기 
                
        if num.out_num == num.max_num:
            break;
print('영업이 마감되었습니다\n')

   
