def vowel_count(str):
    count=0
    vowel=("aeiouAEIOU")
    for alphabet in str:
        if alphabet in vowel:
            count=count+1
        print("No. of Vowels: ",count)
vowel_count("Kartikey IS A GoodBoy")