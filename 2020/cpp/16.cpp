#include <iostream>
#include <fstream>
#include <cstring>
#include <cstdio>

using namespace std;

struct Input
{
    char field[100];
    int a,b,c,d;
};

int part1(Input*, int, int**, int, bool*);
int part2(Input*, int, int**, int, int*, bool*);

int main()
{
    ifstream file(".\\..\\in\\16.txt");

    Input* inp;// = new Input[1];
    int* my_ticket;
    char line[100];

    int SIZE = 0;
    
    // reading ticket info
    file.getline(line,100);
    do
    {
        Input* N = new Input[1 + SIZE];
        for (int i=0; i<SIZE; i++)
        {
            N[i] = inp[i];
        }
        if (SIZE>0) delete[] inp;
        inp = N;

        char f[100];
        strcpy(f, line);
        *(strchr(f, ':')) = '\0';
        strcpy(inp[SIZE].field, f);
        strcpy(line, strchr(line,':')+2);
        
        sscanf(line, "%d-%d or %d-%d",&(inp[SIZE].a),&(inp[SIZE].b),&(inp[SIZE].c),&(inp[SIZE].d));
        file.getline(line,100);
        SIZE++;
    } while (strlen(line)>0);
    
    my_ticket = new int[SIZE];
    
    //reading spare lines
    file.getline(line,100); //reads 'your ticket'
    file.getline(line,100); //reads numbers
    
    //reading my ticket info
    for (int i=0; i<SIZE; i++)
    {
        char f[100];
        strcpy(f,line);
        if (strchr(f,',')!=nullptr) *(strchr(f,',')) = 0;
        my_ticket[i] = atoi(f);
        char* p = strchr(line, ',');
        if (!(p==nullptr)) strcpy(line, strchr(line, ',')+1);
    }

    //spare lines again
    file.getline(line,100); // \n
    file.getline(line,100); // nearby tickets:

    //info about other tickets
    int SIZE_OTHERS = 0;
    int** other_tickets = new int*[243];
    //int** other_tickets = new int*[4];

    for (SIZE_OTHERS = 0; SIZE_OTHERS<243; SIZE_OTHERS++)
    {
        other_tickets[SIZE_OTHERS] = new int[SIZE];

        file.getline(line,100);

        for (int i=0; i<SIZE; i++)
        {
            char f[100];
            strcpy(f,line);
            if (strchr(f,',')!=nullptr) *(strchr(f,',')) = 0;
            other_tickets[SIZE_OTHERS][i] = atoi(f);
            char* p = strchr(line, ',');
            if (!(p==nullptr)) strcpy(line, strchr(line, ',')+1);
        }
    }
    
    bool* val = new bool[SIZE_OTHERS];
    for (int i=0; i<SIZE_OTHERS; i++)
    {
        val[i] = true;
    }

    cout << part1(inp, SIZE, other_tickets, SIZE_OTHERS,val) << endl;
    cout << part2(inp, SIZE, other_tickets, SIZE_OTHERS, my_ticket, val) << endl;


    
    for (int i=0; i<SIZE_OTHERS; i++)
    {
        delete[] other_tickets[i];
    }
    delete[] other_tickets;
    delete[] my_ticket;
    delete[] val;
    delete[] inp;
    file.close();
    return 0;
}

int part1(Input* inp, int sinp, int** other, int sother, bool* val)
{
    int S = 0;
    //array of sinp ints
    for (int i=0; i<sother; i++)
    {
        //one int from other
        for (int j=0; j<sinp; j++)
        {
            bool bo = false;
            int x = other[i][j];
            //struct from inp
            for (int k=0; k<sinp; k++)
            {
                int a = inp[k].a;
                int b = inp[k].b;
                int c = inp[k].c;
                int d = inp[k].d;
                if ((a<=x && x<=b) || (c<=x && x<=d))
                {
                    bo = true;
                    break;
                }    
            }
            if (!bo)
            {
                val[i] = false;
                S+=x;
            }
        }
    }
    return S;
}

int part2(Input* inp, int sinp, int** other, int sother, int* my, bool* val)
{
    /*
    struct pair
    {
        char field[100];
        int cap = 0;
        int* T;
    };
    pair pairs[sinp];
    for (int i =0; i<sinp; i++)
    {
        strcpy(pairs[i].field, inp[i].field);
    }
    //iterating over my ticket values
    for (int i=0; i<sinp; i++)
    {
        int x = my[i];
        //iterating over inp
        for (int j=0; j<sinp; j++)
        {
            Input I = inp[j];
            if ((I.a<=x && x<=I.b) || (I.c<=x && x<=I.d))
            {
                int* newT = new int[pairs[j].cap+1];
                for (int ii=0; ii<pairs[j].cap; ii++)
                {
                    newT[ii] = pairs[j].T[ii];
                }
                newT[pairs[j].cap] = i;
                delete[] pairs[j].T;
                pairs[j].cap++;
                pairs[j].T = newT;
            }
        }

    }
    for (int i=0; i<sinp; i++)
    {
        /*
        for (int j=0; j<pairs[i].cap; j++)
        {
            cout << pairs[i].T[j] << ' ';
        }
        cout << endl;
        
        cout << pairs[i].cap << " ";
    }
    */
    /*
    sprawdzamy czy jest valid ticket

    */
    for (int i=0; i<sother; i++)
    {
        if (val[i] == false)
        {
            continue;
        }

    }
    return 0;
}
/*
    do
    {
        
        Input* N = new Input[1 + SIZE];
        for (int i=0; i<SIZE; i++)
        {
            N[i] = inp[i];
        }
        if (SIZE>0) delete[] inp;
        inp = N;




        /*
        cout << line << endl;
        strcpy(inp[SIZE].field, line);

        file.get();
        file.getline(line,100,'-');
        inp[SIZE].a = atoi(line);
        file.getline(line,100,' ');
        inp[SIZE].b = atoi(line);
        file.get(); //o
        file.get(); //r
        file.get(); // \s
        file.getline(line,100,'-');
        inp[SIZE].c = atoi(line);
        file.getline(line,100);
        inp[SIZE].d = atoi(line);


        
        file.getline(line,100,':');
        cout << line << endl;
        //cout << strlen(line) << endl;
        
        SIZE++;
    } while (strlen(line) > 0);

    //cout << SIZE << endl;
    /*
    for (int i=0; i<SIZE; i++)
    {
        cout << inp[i].field << endl;
    }
    */
    