#include <iostream>
#include <fstream>
#include <cstring>
#include <map>

using namespace std;

struct data
{
    char mask[37] = "\0";
    long long memory_addres=0;
    long long memory_value=0;
};

data* get_input(int&);

long long part1(data*, int);
long long part2(data*, int);

long long result(int, char[37]);

int main()
{
    int input_rows = 15;
    data* input = get_input(input_rows);
    /*
    data* input = new data[input_rows];
    for (int i=0; i<input_rows; i++)
    {
        char t[50];
        cin.getline(t, 50);
        data D;
        if (t[1]=='a') strcpy(D.mask,t+7);
        else
        {
            char* x = strchr(t, ']');
            const int s = (x-t) - 3;
            char temp[s] = {0};
            temp[(x-t) - 2] = '\0';
            strncpy(temp, t+4, (x-t)-4);
            D.memory_addres = atoll(temp);
            D.memory_value = atoll(x+4);
        }
        input[i] = D;
    }
    */
    /*
    for (int i=0; i<input_rows; i++)
    {
        if (input[i].mask[0] != '\0')
        {
            cout << "mask: " << input[i].mask << endl;
        }
        else
        {
            cout << input[i].memory_addres << ": " << input[i].memory_value << endl;
        }
    }
    */

    cout << part1(input, input_rows) << endl;
    //cout << part2(input, input_rows) << endl;


    delete[] input;
}

data* get_input(int& count)
{
    data* P = new data[1];
    
    ifstream input_file(".\\..\\in\\14.txt");

    count = 0;

    char line[50];

    while (input_file.getline(line, 50))
    {
        data* N = new data[count+1];
        for (int i=0; i<count; i++)
        {
            N[i] = P[i];
        }
        delete[] P;
        P = N;

        data D;
        if (line[1]=='a')
        {
            strcpy(D.mask, line+7);
        }
        else
        {
            char* x = strchr(line, ']');
            const int s = (x-line) - 3;
            char temp[s] = {0};
            temp[(x-line) - 2] = '\0';
            strncpy(temp, line+4, (x-line)-4);
            D.memory_addres = atoll(temp);
            D.memory_value = atoll(x+4);
        }
        P[count] = D;
        count++;
    }

    input_file.close();

    return P;
}

long long result(long long value, char mask[37])
{
    char v[37] = {0};
    int i=35;
    while (value)
    {
        v[i] = value & 1;
        value >>= 1;
        i--;
    }

    for (i=0; i<36; i++)
    {
        if (mask[i] == 'X') continue;
        else if (mask[i]=='0') v[i]=0;
        else v[i] = 1;
    }

    long long res = 0;
    long long mult = 1;
    for (i = 35; i>-1; i--)
    {
        long long t = v[i] * mult;
        mult *=2;
        res += t;
    }

    return res;
}

long long part1(data* D, int rows)
{
    map<long long, long long> m;

    long long sum = 0;

    char current_mask[37];

    for (int i=0; i<rows; i++)
    {
        if (D[i].mask[0] !='\0')
        {
            strcpy(current_mask, D[i].mask);
        }
        else
        {
            m[D[i].memory_addres] = result(D[i].memory_value, current_mask);
        }
    }

    
    for (auto i = m.begin(); i!=m.end(); i++)
    {
        sum += i->second;
    }

    return sum;
}



long long part2(data* D, int rows)
{
    map<long long, long long> m;

    for (int i=0; i<rows; i++)
    {
        if (D[i].mask[0]=='\0')
        {
            
        }
        else
        {
            
        }
    }
}