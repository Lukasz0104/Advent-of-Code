#include <iostream>

using namespace std;

int main()
{
    int *tab = new int[200];
    for (int i=0;i<200;i++)
    {
        cin>>tab[i];
    }
    bool f1 = false;
    for (int i=0;i<200;i++)
    {
        for (int j=0; j<200;j++)
        {
            if (i==j) continue;
            if (tab[i]+tab[j]==2020)
            {
                cout<<tab[i]*tab[j]<<endl;
                f1 = true;
                break;
            }
            if (f1) break;
        }
    }
    f1 = false;
    for (int i=0; i<200;i++)
    {
        for (int j=0; j<200;j++)
        {
            if (i==j) continue;
            if (f1) break;
            for (int k=0; k<200;k++)
            {
                if (k==i || k==j) continue;
                if (f1) break;
                if (tab[i]+tab[j]+tab[k]==2020)
                {
                    cout<<tab[i]*tab[j]*tab[k]<<endl;
                    f1 =true;
                    break;
                }
            }
        }
    }

    delete[] tab;
}