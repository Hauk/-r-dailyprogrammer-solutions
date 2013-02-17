/**
 * Challenge 4.
 *
 * You're challenge for today is to create a random password generator!
 * For extra credit, allow the user to specify the amount of passwords to generate.
 * For even more extra credit, allow the user to specify the length of the strings he wants to generate!
 *
 * Finished. Working with extra credit. Only issue is random empty chars are
 * being appended to the password which can decrease the required length. Think
 * it's to do with the mod and srand() generator but I'm done with this one. *
 *
 */

#include <stdlib.h>
#include <iostream>
#include <easy4.h>

using namespace std;

Password::Password()
{
}

vector<string> Password::getPassword(int nPasswords, int nLength)
{
    /*
     * Function does the following:
     * 
     * (1) Generates a number between 1 and 4.
     * (2) Picks an array of either numbers, letters(upper + lower), or symbols.
     * (3) Then uses the rand() function to generate a random index.
     * (4) Then appends the char to a password string.
     * (5) Returns the array full of strings of passwords..
     */

    //Define 4 arrays.
    char plain_upper [] = {'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'};

    char plain_lower [] = {'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'};

    char symbols [] = {'!', '"', '$', '%', '^', '&', '(', ')', '<', '>', '?', '#', '[', ']'};

    char nums [] = {'1', '2', '3', '4', '5', '6', '7', '8', '9', '0'};

    //Define a string vector to hold our passwords.
    vector<string> results;

    string finalPassword = "";
    int switchOne = 0;

    srand((unsigned)time(NULL));

    //Loop for required number of passwords.
    for(int i = 0; i < nPasswords; i++)
    {        
        for(int k = 0; k < nLength; k++)
        {
            switchOne = rand() % 4;

           //Choose a char from 1 of the arrays based on switchOne.
            if(switchOne == 1)
            {
                finalPassword += plain_upper[(rand() % 26) - 1];
            }
            else if(switchOne == 2)
            {
                finalPassword += plain_lower[(rand() % 26) - 1];
            }
            else if(switchOne == 3)
            {
                finalPassword += symbols[(rand() % 14) - 1];
            }
            else
            {
                finalPassword += nums[(rand() % 10) - 1];
            }
        }
        results.push_back(finalPassword);
        finalPassword = "";
    }   

    return results;
}

int main()
{
    Password* pdGenerator = new Password();
    int num_Passwords = 0;
    int pLength = 0;

    cout << "Please enter the number of passwords to generate: ";

    cin >> num_Passwords;

    pdGenerator->setNumPasswords(num_Passwords);

    cout << "Please enter a number for the length required for each password(e.g. 12 characters): ";

    cin >> pLength;

    pdGenerator->setOrigPasswdLength(pLength);

    vector<string> pwResults = pdGenerator->getPassword(num_Passwords, pLength);

    //THIS BUTTON SHOVES THE STUFF OUT!
    for(int i = 0; i != pwResults.size(); i++)
    {
        cout << "Password #" << (i + 1) << " is: " << pwResults[i] << endl;
    }
}

