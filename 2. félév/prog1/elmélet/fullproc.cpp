#include <iostream>
#include <thread>
using namespace std;

void workerFunction() {
    while (true) {
        
    }
}

int main() {
    const int numThreads = thread::hardware_concurrency();

    for (int i = 0; i < numThreads; ++i) {
        thread(workerFunction).detach();
    }

    this_thread::sleep_for(chrono::seconds(10));

    return 0;
}
