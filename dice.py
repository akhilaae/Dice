import random
def roll_dice():
    min=1
    max=6
    roll_again='y'
    while roll_again.lower()=='y' or roll_again.lower()=='yes':
        num=int(input("Enter no of dice : "))
        sum=0
        dice=[]
        for i in range(0,num):
            dice_value=random.randrange(min,max)
            dice.append(dice_value)
            sum+=dice_value
        print("dice = ", dice, "sum = ", sum)
        roll_again=input("Roll again(y/n or yes/no)?")
if __name__ == '__main__':
   roll_dice()
