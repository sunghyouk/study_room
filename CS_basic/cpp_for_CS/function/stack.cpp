# include <iostream>
using namespace std;

int test(int a, int b);

int main(void)
{
    int a = 10, b = 5;
    int res = test(a, b);
    cout << "result of test : " << res << endl;
    return 0;
}

int test(int a, int b)
{
    int c = a + b;
    int d = a - b;
    return c + d;
}