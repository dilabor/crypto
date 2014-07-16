#!/usr/bin/env python

"""
@copyright: AlertAvert.com (c) 2012. All rights reserved.

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

   http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.

Collection of code utilities developed while following the Crypt course on
Coursera.org:
    https://class.coursera.org/crypto-2012-002/class/index

@author: Marco Massenzio (m.massenzio@gmail.com)
         Created on Jul 14, 2012
"""
from Crypto.Util.strxor import strxor


def xor(a, b):
    max_len = min(len(a), len(b))
    return strxor(a[:max_len], b[:max_len])


# Week 1 - Problem set
def resolve_q7():
    cipher = r'6c73d5240a948c86981bc294814d'.decode('hex')
    plaintext = r'attack at dawn'
    key = xor(cipher, plaintext)

    # Encode the new secret message
    plaintext = r'attack at dusk'
    cipher = xor(key, plaintext.encode('hex'))
    print cipher.encode('hex')


####
# Programming assignment
####
CIPHER_TEXTS = [hex_.decode('hex') for hex_ in [
    r'315c4eeaa8b5f8aaf9174145bf43e1784b8fa00dc71d885a804e5ee9fa40b16349c146fb778cdf2d3aff021dfff5b403b510d0d0455468'
    r'aeb98622b137dae857553ccd8883a7bc37520e06e515d22c954eba5025b8cc57ee59418ce7dc6bc41556bdb36bbca3e8774301fbcaa3b8'
    r'3b220809560987815f65286764703de0f3d524400a19b159610b11ef3e',

    r'234c02ecbbfbafa3ed18510abd11fa724fcda2018a1a8342cf064bbde548b12b07df44ba7191d9606ef4081ffde5ad46a5069d9f7f543bed'
    r'b9c861bf29c7e205132eda9382b0bc2c5c4b45f919cf3a9f1cb74151f6d551f4480c82b2cb24cc5b028aa76eb7b4ab24171ab3cdad'
    r'b8356f',

    r'32510ba9a7b2bba9b8005d43a304b5714cc0bb0c8a34884dd91304b8ad40b62b07df44ba6e9d8a2368e51d04e0e7b207b70b9b826'
    r'1112bacb6c866a232dfe257527dc29398f5f3251a0d47e503c66e935de81230b59b7afb5f41afa8d661cb',

    r'32510ba9aab2a8a4fd06414fb517b5605cc0aa0dc91a8908c2064ba8ad5ea06a029056f47a8ad3306ef5021eafe1ac01a81197847a5c68'
    r'a1b78769a37bc8f4575432c198ccb4ef63590256e305cd3a9544ee4160ead45aef520489e7da7d835402bca670bda8eb775200b8dabbba'
    r'246b130f040d8ec6447e2c767f3d30ed81ea2e4c1404e1315a1010e7229be6636aaa',

    r'3f561ba9adb4b6ebec54424ba317b564418fac0dd35f8c08d31a1fe9e24fe56808c213f17c81d9607cee021dafe1e001b21ade877a5e68b'
    r'ea88d61b93ac5ee0d562e8e9582f5ef375f0a4ae20ed86e935de81230b59b73fb4302cd95d770c65b40aaa065f2a5e33a5a0bb5dcaba437'
    r'22130f042f8ec85b7c2070',

    r'32510bfbacfbb9befd54415da243e1695ecabd58c519cd4bd2061bbde24eb76a19d84aba34d8de287be84d07e7e9a30ee714979c7e1123a'
    r'8bd9822a33ecaf512472e8e8f8db3f9635c1949e640c621854eba0d79eccf52ff111284b4cc61d11902aebc66f2b2e436434eacc0aba938'
    r'220b084800c2ca4e693522643573b2c4ce35050b0cf774201f0fe52ac9f26d71b6cf61a711cc229f77ace7aa88a2f19983122b11be87a59'
    r'c355d25f8e4',

    r'32510bfbacfbb9befd54415da243e1695ecabd58c519cd4bd90f1fa6ea5ba47b01c909ba7696cf606ef40c04afe1ac0aa8148dd066592de'
    r'd9f8774b529c7ea125d298e8883f5e9305f4b44f915cb2bd05af51373fd9b4af511039fa2d96f83414aaaf261bda2e97b170fb5cce2a53e'
    r'675c154c0d9681596934777e2275b381ce2e40582afe67650b13e72287ff2270abcf73bb028932836fbdecfecee0a3b894473c1bbeb6b49'
    r'13a536ce4f9b13f1efff71ea313c8661dd9a4ce',

    r'315c4eeaa8b5f8bffd11155ea506b56041c6a00c8a08854dd21a4bbde54ce56801d943ba708b8a3574f40c00fff9e00fa1439fd0654327a'
    r'3bfc860b92f89ee04132ecb9298f5fd2d5e4b45e40ecc3b9d59e9417df7c95bba410e9aa2ca24c5474da2f276baa3ac325918b2daada43d'
    r'6712150441c2e04f6565517f317da9d3',

    r'271946f9bbb2aeadec111841a81abc300ecaa01bd8069d5cc91005e9fe4aad6e04d513e96d99de2569bc5e50eeeca709b50a8a987f4264e'
    r'db6896fb537d0a716132ddc938fb0f836480e06ed0fcd6e9759f40462f9cf57f4564186a2c1778f1543efa270bda5e933421cbe88a4a522'
    r'22190f471e9bd15f652b653b7071aec59a2705081ffe72651d08f822c9ed6d76e48b63ab15d0208573a7eef027',

    r'466d06ece998b7a2fb1d464fed2ced7641ddaa3cc31c9941cf110abbf409ed39598005b3399ccfafb61d0315fca0a314be138a9f32503be'
    r'dac8067f03adbf3575c3b8edc9ba7f537530541ab0f9f3cd04ff50d66f1d559ba520e89a2cb2a83']
]

SECRET = r'32510ba9babebbbefd001547a810e67149caee11d945cd7fc81a05e9f85aac650e9052ba6a8cd8257bf14d13e6f0a803b54fd' \
         r'e9e77472dbff89d71b57bddef121336cb85ccb8f3315f4b52e301d16e9f52f904'.decode('hex')


#: Before running the main() code (which will yield the secret) run a sweep() and manually fill as
#: many blanks as possible, and fill in GUESS
GUESS = 'The secret message is ************* stream ciphers never use the key more than once'

#: This can then be guessed and the blanks filled in by running the main()
MSG_8 = 'A (private-key)  encryption scheme states 3 algorithms, namely a procedure for gene'


def sweep():
    """ This is executed first, to get an initial guess for the SECRET.

        The idea is to extract as much information as possible, with as little effort as possible,
        by XORing the encrypted secret with all other encrypted messages, and find out as many
        characters of the secret.

        A manual pass is necessary afterwards to 'fill the blanks' and correct wrong guesses (
        where the secret has spaces and we guess the alpha char of the other message instead).

        :return: This yields a good approximations with only around 10 characters in the middle
        unguessable (see ```GUESS```).
    """
    guess = ['*' for _ in xrange(0, len(SECRET) / 2)]
    for c in CIPHER_TEXTS:
        scramble = xor(c, SECRET)
        for i, c in enumerate(scramble):
            if 31 < ord(c) < 127:
                guess[i] = c.swapcase()
            elif c == r'\x00':
                guess[i] = ' '
    return ''.join(guess)


def guess_key():
    """ This is executed next: by XORing the guessed secret with its encrypted counterpart,
    we get an initial guess for the KEY - there will be incorrect guesses where GUESS has '*'s,
    but given that the nature of XOR encoding, the errors are localized, and can be corrected.

    :return: a guess for the encryption key
    """
    return xor(SECRET, GUESS)


def guess_key_fully():
    """ Once we have all the decrypted messages, we can get a stab at manually filling the
    remaining gaps, and improve our guess of the key: as it happens, MSG_8 can be fully guessed
    correctly, at which point the encryption key can be fully guessed.

    :return: the encryption key
    """
    return xor(CIPHER_TEXTS[8], MSG_8)


def get_messages(key):
    """ Helper method to decrypt all messages with the given ```key```

    :param key: the encryption key
    :return: a list of decrypted messages
    """
    messages = [xor(key, encrypted) for encrypted in CIPHER_TEXTS]
    return messages


def main():
    guesses = get_messages(guess_key())
    for i, msg in enumerate(guesses):
        print('{}: [{}]'.format(i, msg))

    print '==='
    for i, secret in enumerate(CIPHER_TEXTS):
        junk = xor(CIPHER_TEXTS[8], secret)
        guess = [c for c in guesses[8]]
        for j, c in enumerate(junk):
            if c.isalpha() and 20 < j < 37:
               guess[j] = c.swapcase()
        print i, ''.join(guess)
    print '==='
    key = xor(CIPHER_TEXTS[8], MSG_8)
    decrypted_secret = xor(key, SECRET)
    print(decrypted_secret)

if __name__ == '__main__':
    main()
