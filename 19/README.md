# Getting `google-re2` to work

```
brew install re2 absl pybind

# Note: *CXX*FLAGS, not *C*FLAGS
CXXFLAGS="-std=c++17 -I$(brew --prefix)/include" LDFLAGS="-L$(brew --prefix)/lib" pipenv install google-re2
```
