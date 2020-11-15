# Poker winning_hand

Winning hand takes all hands in deck as arguments, 
evaluates and returns the hand with highest rank. 

## Usage
A card is represented as short of '{card_name}{suite_name}'.  
Ex. AS = Ace Spade, 10c = 10 club, qd = Queen diamond  
A hand is passed as set of cards in string separated by spaces

```shell
python winning_hand.py 'As Ah 8c Jd Qs' 'Js 8h Qc Kd Ks' 
#returns The winning hand is --> (Spade A, Heart A, Club 8, Diamond J, Spade Q)

python winning_hand.py 'As Ah 8c Jd Qs' 'Js 8h Qc Ad As'
#returns The winning hand is --> It's a tie

python winning_hand.py 'As Ah 8c Jd Qs' '8s 8h Qc Ad As'
#returns The winning hand is --> (Spade 8, Heart 8, Club Q, Diamond A, Spade A)

python winning_hand.py 'As Ah Ac Jd Qs' '8s 8h Qc Ad As' 'Js Jh Jc 2d 2s'
#returns The winning hand is --> (Spade J, Heart J, Club J, Diamond 2, Spade 2)
```

## License
[MIT](https://choosealicense.com/licenses/mit/)