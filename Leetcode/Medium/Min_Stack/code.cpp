class MinStack {
public:
    stack<int> st;
    stack<int> minSt;
    MinStack() {
        
    }

    void push(int val) {
        st.push(val);
    }

    void pop() {
        st.pop();
    }

    int top() {
        return st.top();
    }

    int getMin() {
        int min = st.top();
        while (!st.empty()) {
            minSt.push(st.top());
            st.pop();
            if (min >= minSt.top()) { min = minSt.top(); }
        }

        while (!minSt.empty()) {
            st.push(minSt.top());
            minSt.pop();
        }
        return min;
    }
};