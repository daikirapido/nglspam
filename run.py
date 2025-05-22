import requests
import time
from threading import Thread

def ngl_spam():
    print("\033[1;33mEnter details one by one:\033[0m")
    username = input("\033[1;32mUsername: \033[0m")
    msg = input("\033[1;32mMessage: \033[0m")
    interval = input("\033[1;32mInterval (seconds, default 2): \033[0m") or "2"
    amount = input("\033[1;32mAmount (default 999): \033[0m") or "999"

    interval = float(interval)
    amount = int(amount)

    print(f"\n\033[1;33mStarting NGL spam to {username}...\033[0m")
    print(f"\033[1;34mMessage: {msg}\033[0m")
    print(f"\033[1;34mInterval: {interval}s | Amount: {amount}\033[0m\n")
    
    def spam():
        count = 0
        while count < amount:
            headers = {
                'referer': f'https://ngl.link/{username}',
                'accept-language': 'tr-TR,tr;q=0.9,en-US;q=0.8,en;q=0.7',
            }
            
            data = {
                'username': username,
                'question': msg,
                'deviceId': 'ea356443-ab18-4a49-b590-bd8f96b994ee',
                'gameSlug': '',
                'referrer': '',
            }
            
            try:
                response = requests.post('https://ngl.link/api/submit', data=data, headers=headers)
                count += 1
                print(f"\033[1;32m[{count}/{amount}] Sent to {username}\033[0m")
            except Exception as e:
                print(f"\033[1;31mError: {str(e)[:50]}...\033[0m")
            
            time.sleep(interval)
        
        print(f"\n\033[1;36m✅ Spam complete! Sent {count} messages to {username}\033[0m")
        print("\033[1;35mCredits: rapido\033[0m")
    
    Thread(target=spam).start()

if __name__ == "__main__":
    ngl_spam()