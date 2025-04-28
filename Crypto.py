import hashlib

def generate_primes(n):
    primes = []
    i = 2
    while len(primes) < n:
        if all(i % p != 0 for p in primes):
            primes.append(i)
        i += 1
    return primes

#utilser haslib pour crypter salt
def derive_key(salt, length):
    hash_obj = hashlib.sha256(salt.encode())
    key = hash_obj.digest()
    while len(key) < length:
        hash_obj.update(key)
        key += hash_obj.digest()
    return list(key[:length])

def encrypt(phrase, salt):
    primes = generate_primes(len(phrase))
    key = derive_key(salt, len(phrase))
    
    encrypted = []
    cumulative = 0

    for i, char in enumerate(phrase):
        p = primes[i]
        k = key[i]
        shifted = (ord(char) + p + k + cumulative) % 256
        encrypted.append(shifted)
        cumulative = (cumulative + shifted) % 256 

    return encrypted

def decrypt(encrypted, salt):
    primes = generate_primes(len(encrypted))
    key = derive_key(salt, len(encrypted))

    decrypted = ''
    cumulative = 0

    for i, val in enumerate(encrypted):
        p = primes[i]
        k = key[i]
        orig = (val - p - k - cumulative) % 256
        decrypted += chr(orig)
        cumulative = (cumulative + val) % 256

    return decrypted


#Utilisation
phrase = "Bonjour, c'est un test d'encryptage grâce à ce petit algorithme fait maison"
salt = "AjvfklvjklbBFIEHZOI54564"


chiffre = [54, 13, 175, 139, 121, 0, 22, 207, 67, 20, 62, 61, 184, 73, 223, 81, 174, 191, 64, 243, 104, 208, 231, 74, 210, 140, 252, 95, 153, 99, 101, 217, 85, 227, 240, 37, 45, 203, 120, 
105, 110, 229, 213, 185, 61, 123, 194, 17, 196, 49, 162, 71, 156, 109, 167, 179, 122, 172, 162, 191, 182, 248, 127, 12, 19, 31, 5, 159, 30, 187, 36, 150, 197, 160, 114]
# chiffre = encrypt(phrase, salt)
# print("Chiffré :", chiffre)

dechiffre = decrypt(chiffre, salt)
print("Déchiffré :", dechiffre)