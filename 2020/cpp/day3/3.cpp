#include <iostream>

using namespace std;

int main()
{
    int counter1 = 0;
    int cnt = 0;
    char c[324][32];
    cin.getline(c[cnt],32);
    while(c[cnt][0]!='\0')
    {
        cnt++;
        cin.getline(c[cnt],32);
    }
    //part 1
    int x=0;
    for (int i=0; i<323; i++)
    {
        if (c[i][x%31]=='#') counter1++;
        x+=3;
    }
    cout<<counter1<<endl;

    //part 2
    int results[5] = {0,0,0,0,0};
    int slopes[5][2] = {{1,1},{3,1},{5,1},{7,1},{1,2}};
    
    for (int i=0; i<5;i++)
    {
        int x=0;
        for (int j=0; j<323;j+=slopes[i][1])
        {
            if (c[j][x%31]=='#') results[i]++;
            x+=slopes[i][0];
        }
    }
    //for (int i=0; i<5;i++) cout<<results[i]<<endl;
    cout<<1LL * results[0]*results[1]*results[2]*results[3]*results[4]<<endl;
}