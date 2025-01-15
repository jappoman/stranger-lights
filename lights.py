# Libraries
import time
import random
import board
import neopixel

#Start up random seed
random.seed()

# Choose an open pin connected to the Data In of the NeoPixel strip, i.e. board.D18
# NeoPixels must be connected to D10, D12, D18 or D21 to work.
pixel_pin = board.D18

# The number of NeoPixels
num_pixels = 100

# The order of the pixel colors - RGB or GRB. Some NeoPixels have red and green reversed!
# For RGBW NeoPixels, simply change the ORDER to RGBW or GRBW.
ORDER = neopixel.RGB

pixels = neopixel.NeoPixel(pixel_pin, num_pixels, brightness=0.2, auto_write=False, pixel_order=ORDER)

def rainbow_cycle(wait):
    for j in range(255):
        for i in range(num_pixels):
            pixel_index = (i * 256 // num_pixels) + j
            pixels[i] = wheel(pixel_index & 255)
        pixels.show()
        time.sleep(wait)


# My functions

def init():
	pixels.fill((0, 0, 0))
	pixels.show()

def test():
	for i in range(num_pixels):
		pixels.fill((0, 0, 0))
		pixels.show()
		time.sleep(0.1)
		pixels[i]=(random.randint(0,255), random.randint(0,255), random.randint(0,255))
		pixels.show()
		time.sleep(0.1)
	time.sleep(0.1)
	pixels.fill((0, 0, 0))
	pixels.show()

def lights_all_sequence():
	pixels.fill((0, 0, 0))
	pixels.show()
	for i in range(num_pixels):
		pixels[i]=(random.randint(0,255), random.randint(0,255), random.randint(0,255))
		pixels.show()
		time.sleep(0.1)
	time.sleep(1)

def lights_all_sequence_reverse():
	pixels.fill((0, 0, 0))
	pixels.show()
	for i in range(num_pixels-1, 0, -1):
		pixels[i]=(random.randint(0,255), random.randint(0,255), random.randint(0,255))
		pixels.show()
		time.sleep(0.1)
	time.sleep(1)

def random_ordinated_lights():
	for i in range(4):
		for j in range(num_pixels):
			pixels[j]=(random.randint(0,255), random.randint(0,255), random.randint(0,255))
		pixels.show()
		time.sleep(1)
	time.sleep(1)

def crazy_lights_fade_out():
	for i in range(random.randint(2,5)):
		for j in range(num_pixels):
			pixels[j]=(random.randint(0,255), random.randint(0,255), random.randint(0,255))
		pixels.show()
		time.sleep(random.randint(0,1))
		pixels.fill((0, 0, 0))
		pixels.show()
	time.sleep(random.randint(0,1))
	pixels.fill((0, 0, 0))
	pixels.show()

def crazy_lights_fade_in():
	for i in range(random.randint(2,5)):
		pixels.fill((0, 0, 0))
		pixels.show()
		for j in range(num_pixels):
			pixels[j]=(random.randint(0,255), random.randint(0,255), random.randint(0,255))
		pixels.show()
		time.sleep(random.randint(0,1))
	time.sleep(random.randint(0,1))

def spelling(sleep_time):
	for line in words_list:
		tospell=list(line)
		i=0
		time.sleep(sleep_time)
		for c in tospell:
			time.sleep(sleep_time)
			pixels.fill((0, 0, 0))
			pixels.show()
			time.sleep(sleep_time)

			if tospell[i]==' ':
				print (" ")
				pixels.fill((0, 0, 0))
				pixels.show()

			elif tospell[i]=='a' or tospell[i]=='A':
				print ("a")
				for j in range(len(A)):
					pixels[A[j]]=(random.randint(0,255),random.randint(0,255),random.randint(0,255))
				pixels.show()

			elif tospell[i]=='b' or tospell[i]=='B':
				print ("b")
				for j in range(len(B)):
					pixels[B[j]]=(random.randint(0,255),random.randint(0,255),random.randint(0,255))
				pixels.show()

			elif tospell[i]=='c' or tospell[i]=='C':
				print ("c")
				for j in range(len(C)):
					pixels[C[j]]=(random.randint(0,255),random.randint(0,255),random.randint(0,255))
				pixels.show()

			elif tospell[i]=='d' or tospell[i]=='D':
				print ("d")
				for j in range(len(D)):
					pixels[D[j]]=(random.randint(0,255),random.randint(0,255),random.randint(0,255))
				pixels.show()

			elif tospell[i]=='e' or tospell[i]=='E':
				print ("e")
				for j in range(len(E)):
					pixels[E[j]]=(random.randint(0,255),random.randint(0,255),random.randint(0,255))
				pixels.show()

			elif tospell[i]=='f' or tospell[i]=='F':
				print ("f")
				for j in range(len(F)):
					pixels[F[j]]=(random.randint(0,255),random.randint(0,255),random.randint(0,255))
				pixels.show()

			elif tospell[i]=='g' or tospell[i]=='G':
				print ("g")
				for j in range(len(G)):
					pixels[G[j]]=(random.randint(0,255),random.randint(0,255),random.randint(0,255))
				pixels.show()

			elif tospell[i]=='h' or tospell[i]=='H':
				print ("h")
				for j in range(len(H)):
					pixels[H[j]]=(random.randint(0,255),random.randint(0,255),random.randint(0,255))
				pixels.show()

			elif tospell[i]=='i' or tospell[i]=='I':
				print ("i")
				for j in range(len(I)):
					pixels[I[j]]=(random.randint(0,255),random.randint(0,255),random.randint(0,255))
				pixels.show()

			elif tospell[i]=='j' or tospell[i]=='J':
				print ("j")
				for j in range(len(J)):
					pixels[J[j]]=(random.randint(0,255),random.randint(0,255),random.randint(0,255))
				pixels.show()

			elif tospell[i]=='k' or tospell[i]=='K':
				print ("k")
				for j in range(len(K)):
					pixels[K[j]]=(random.randint(0,255),random.randint(0,255),random.randint(0,255))
				pixels.show()

			elif tospell[i]=='l' or tospell[i]=='L':
				print ("l")
				for j in range(len(L)):
					pixels[L[j]]=(random.randint(0,255),random.randint(0,255),random.randint(0,255))
				pixels.show()

			elif tospell[i]=='m' or tospell[i]=='M':
				print ("m")
				for j in range(len(M)):
					pixels[M[j]]=(random.randint(0,255),random.randint(0,255),random.randint(0,255))
				pixels.show()

			elif tospell[i]=='n' or tospell[i]=='N':
				print ("n")
				for j in range(len(N)):
					pixels[N[j]]=(random.randint(0,255),random.randint(0,255),random.randint(0,255))
				pixels.show()

			elif tospell[i]=='o' or tospell[i]=='O':
				print ("o")
				for j in range(len(O)):
					pixels[O[j]]=(random.randint(0,255),random.randint(0,255),random.randint(0,255))
				pixels.show()

			elif tospell[i]=='p' or tospell[i]=='P':
				print ("p")
				for j in range(len(P)):
					pixels[P[j]]=(random.randint(0,255),random.randint(0,255),random.randint(0,255))
				pixels.show()

			elif tospell[i]=='q' or tospell[i]=='Q':
				print ("q")
				for j in range(len(Q)):
					pixels[Q[j]]=(random.randint(0,255),random.randint(0,255),random.randint(0,255))
				pixels.show()

			elif tospell[i]=='r' or tospell[i]=='R':
				print ("r")
				for j in range(len(R)):
					pixels[R[j]]=(random.randint(0,255),random.randint(0,255),random.randint(0,255))
				pixels.show()

			elif tospell[i]=='s' or tospell[i]=='S':
				print ("s")
				for j in range(len(S)):
					pixels[S[j]]=(random.randint(0,255),random.randint(0,255),random.randint(0,255))
				pixels.show()

			elif tospell[i]=='t' or tospell[i]=='T':
				print ("t")
				for j in range(len(T)):
					pixels[T[j]]=(random.randint(0,255),random.randint(0,255),random.randint(0,255))
				pixels.show()

			elif tospell[i]=='u' or tospell[i]=='U':
				print ("u")
				for j in range(len(U)):
					pixels[U[j]]=(random.randint(0,255),random.randint(0,255),random.randint(0,255))
				pixels.show()

			elif tospell[i]=='v' or tospell[i]=='V':
				print ("v")
				for j in range(len(V)):
					pixels[V[j]]=(random.randint(0,255),random.randint(0,255),random.randint(0,255))
				pixels.show()

			elif tospell[i]=='w' or tospell[i]=='W':
				print ("w")
				for j in range(len(W)):
					pixels[W[j]]=(random.randint(0,255),random.randint(0,255),random.randint(0,255))
				pixels.show()

			elif tospell[i]=='x' or tospell[i]=='X':
				print ("x")
				for j in range(len(X)):
					pixels[X[j]]=(random.randint(0,255),random.randint(0,255),random.randint(0,255))
				pixels.show()

			elif tospell[i]=='y' or tospell[i]=='Y':
				print ("y")
				for j in range(len(Y)):
					pixels[Y[j]]=(random.randint(0,255),random.randint(0,255),random.randint(0,255))
				pixels.show()

			elif tospell[i]=='z' or tospell[i]=='Z':
				print ("z")
				for j in range(len(Z)):
					pixels[Z[j]]=(random.randint(0,255),random.randint(0,255),random.randint(0,255))
				pixels.show()

			else:
				pixels.fill((0, 0, 0))
				pixels.show()
			i=i+1

	time.sleep(sleep_time)
	pixels.fill((0, 0, 0))
	pixels.show()

def orange_portal(exclusion):
    #filling the portal
    actual_color=((random.randint(120,180),random.randint(40,70),0))
    for i in range(exclusion, num_pixels):
        if i%3==0:
            actual_color=((random.randint(120,180),random.randint(40,70),0))
        pixels[i]=actual_color

    #rotating
    for i in range(100):
        temppixel = pixels[exclusion]
        for j in range(exclusion, num_pixels-1, 1):
            pixels[j]=pixels[j+1]
        pixels[num_pixels-1]=temppixel
        pixels.show()
        time.sleep(0.03)

def blue_portal(exclusion):
    #filling the portal
    actual_color=((0,random.randint(30,100),random.randint(120,250)))
    for i in range(exclusion, num_pixels):
        if i%3==0:
            actual_color=((0,random.randint(30,100),random.randint(120,250)))
        pixels[i]=actual_color

    #rotating
    for i in range(100):
        temppixel=pixels[num_pixels-1]
        for j in range(num_pixels-1, exclusion, -1):
            pixels[j]=pixels[j-1]
        pixels[exclusion]=temppixel
        pixels.show()
        time.sleep(0.03)



# My program

init()

while True:

#	from letterlist import *

#	lights_all_sequence()
#	random_ordinated_lights()
#	crazy_lights_fade_out()

    init()
    orange_portal(29)
#    time.sleep(0.5)
    init()
    blue_portal(29)
#    time.sleep(0.5)

#	words_list  = open("/home/pi/wordslist.txt", "r")
#	spelling(0.5)
#	words_list.close()
#	time.sleep(1.3)

#	crazy_lights_fade_in()
#	random_ordinated_lights()
#	lights_all_sequence_reverse()
