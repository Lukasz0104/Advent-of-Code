#include <iostream>
#include <cstdio>
#include <algorithm>

using namespace std;

int process(char c[11])
{
    int r=0;
    int p=1;
    for (int i=6; i>=0;i--)
    {
        r = r + (c[i]=='B'? p : 0);
        p*=2;
    }
    r = 8*r;
    p=4;
    for (int i=7;i<10;i++)
    {
        r += (c[i]=='R'? p : 0);
        p/=2;
    }
    return r;
}

int main()
{
    int m = 0;
    char s[11];
    int t[843];
    cin.getline(s,11);
    int i=0;
    while (s[0]!='\0')
    {
        int k = process(s);
        t[i++]=k;
        if (k>m) m=k;
        cin.getline(s,11);
    }
    cout << m << endl;
    sort(t, t+843);
    for (int i=1; i<842; i++)
    {
        if (t[i+1]-t[i]==2)
        {
            if (t[i]>64)
            {
                cout<<t[i]+1<<endl;
                break;
            }
        }
    }
}