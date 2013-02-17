#ifndef PASSWORD_H_
#define PASSWORD_H_

/**
 * Challenge #4.
 *
 * You're challenge for today is to create a random password generator!
 * For extra credit, allow the user to specify the amount of passwords to
 * generate.
 * For even more extra credit, allow the user to specify the length of the
 * strings he wants to generate!
 *
 * Finished and working with extra credit. Only issue is empty characters are being appended to
 * the password, so it changes the length. 
 *
 */

#include <stdio.h>
#include <string>
#include <iostream>
#include <vector>

using namespace std;

class Password
{
    public:
        
        Password();
        ~Password();

        void setNumPasswords(int newAmount) { numPasswords = newAmount; };
        void setOrigPasswdLength(int passwdLen) { passwdLength = passwdLen; };
        void setPasswords(string passwords []) {};

        int getNumPasswordsToGenerate() { return numPasswords; };
        int getPassWordLength() { return passwdLength; };

        vector<string> getPassword(int numPasswds, int passwdLen);

    private:

        string passwords [];
        int numPasswords;
        int passwdLength;
};

#endif /* PASSWORD_H_ */
