#include <iostream>

using namespace std;

int main()
{
    const char fields[8][4] = 
    {
        "byr","iyr","eyr","hgt","hcl","ecl","pid","cid"
    };
    char lines[953][100];
    char counter1 = 0;
    for (int i=0; i<953; i++)
    {
        cin.getline(lines[i],100);
    }
    char temp[300];

    for (int i=0; i<953; i++)
    {
        if (lines[i][0]=='\n')
        {
            temp[0] = '\0';
        }
        else
        {
            
        }
        
    }
}