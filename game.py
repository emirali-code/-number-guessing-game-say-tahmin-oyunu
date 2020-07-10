print("Sayı Tahmin Oyununa Hoş geldiniz")
from playsound import playsound
playsound('WINDOWS ERROR  REMIX.mp3')


giriş=input(" \nNasıl Oynanır:\nBilgisayar 1 ile 100 arasında bir sayı tutar \nOyuncu Bilgisayarın tuttuğu sayıyı bulmaya çalışır\n\nOyuna Devam Etmek İçin Enter'e Basınız")
if giriş==(""):
    print("-----YÜKLENİYOR-----")
import time

time.sleep(2)


bulmahakkı=0 
while True:

    from random import randint
    x = randint (1,100)
    tahmin = False
    while not tahmin:
        try:
            
            Sayı=int(input("Bir sayı Tahmin ediniz. : "))
        
        except ValueError:
            print("Lütfen Geçerli bir sayı girin.")
            continue
        if Sayı> x + 20 :
            bulmahakkı -=1
            from playsound import playsound
            playsound('Bruh Sound Effect 2.mp3')
            print("Tahmin Ettiğiniz Sayı Çok Büyük.")
            
                
        
            
        elif  Sayı>x:
            bulmahakkı -=1
            from playsound import playsound
            playsound('Bruh Sound Effect 2.mp3')
            print("Tahmin Ettiğiniz Sayı Büyük.")
            
                
        
            
        elif Sayı  < x - 20  :
            bulmahakkı -=1
            from playsound import playsound
            playsound('Bruh Sound Effect 2.mp3')
            print("Tahmin Ettiğiniz Sayı Çok Küçük.")
            
                
        
            
        elif Sayı<x:
            bulmahakkı -=1
            from playsound import playsound
            playsound('Bruh Sound Effect 2.mp3')
            print("Tahmin Ettiğiniz Sayı Küçük.")
            
                        
        elif bulmahakkı == -3:
            input("Kaybettiniz Enter'e Basarak Yeniden Oynayabilirsiniz")
        
            

    
        else:
            tahmin=True
        
            from playsound import playsound
            playsound('doru ses efekti.mp3')
        
            print("Tebrikler Kazandınız Bilgisayarın Tuttuğu Sayıyı Buldunuz")
            çıkış=int(input("\n \n1'e Basrak Yeniden Oynayabilir 2'ye basarak çıkabilirsiniz. \n"))
            if çıkış==(1):
                continue
            if çıkış==(2):
                quit()
        
           




