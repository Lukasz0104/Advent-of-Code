#include <cstdio>
#include <string>
#include <iostream>
using namespace std;

int main()
{
    int count1 = 0;
    int count2 = 0;
    int a, b;
    char tab[100];
    char s[100];
    char c;
    cin.getline(s,100);
    while (s[0]!='\0')
    {
        sscanf(s, "%d-%d %c: %s", &a, &b, &c, &tab);
        //part 1
        int i=0;
        int c1=0;
        while (tab[i]!='\0')
        {
            if (tab[i]==c)
            {
                c1++;
            }
            i++;
        }
        if (a<=c1 && c1<=b) count1++;

        //part 2
        if ((tab[a-1]==c && tab[b-1]!=c) || (tab[b-1]==c && tab[a-1]!=c)) count2++;


        cin.getline(s,100);
    }
    cout<<count1<<endl;
    cout<<count2<<endl;
}