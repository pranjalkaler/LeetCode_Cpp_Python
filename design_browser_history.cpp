class BrowserHistory {

    std :: deque<std :: string> history;
    int currentPage;
public:
    BrowserHistory(string homepage) {
        history.push_back(homepage);
        currentPage = 0;
    }

    void visit(string url) {
        while(currentPage != history.size() - 1)
            history.pop_back();

        history.push_back(url);
        ++currentPage;
    }

    string back(int steps) {
        while(steps && currentPage) {
            currentPage--;
            steps--;
        }
        return history[currentPage];
    }

    string forward(int steps) {
        while(steps && currentPage < history.size() - 1) {
            currentPage++;
            steps--;
        }
        return history[currentPage];
    }
};


/**
 * Your BrowserHistory object will be instantiated and called as such:
 * BrowserHistory* obj = new BrowserHistory(homepage);
 * obj->visit(url);
 * string param_2 = obj->back(steps);
 * string param_3 = obj->forward(steps);
 */