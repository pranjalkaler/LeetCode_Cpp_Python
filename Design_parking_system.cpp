class ParkingSystem {
    int _big, _medium, _small;
public:
    ParkingSystem(int big, int medium, int small) : _big(big), _medium(medium), _small(small) {
        
    }
    
    bool addCar(int carType) {
        switch(carType) {
            case 1:
                if(_big) {
                    --_big;
                    return true;
                }
                return false;
                break;
            case 2:
                if(_medium) {
                    --_medium;
                    return true;
                }
                return false;
                break;
            case 3:
                if(_small) {
                    --_small;
                    return true;
                }
                return false;
                break;
        }
        return false;
    }
};

/**
 * Your ParkingSystem object will be instantiated and called as such:
 * ParkingSystem* obj = new ParkingSystem(big, medium, small);
 * bool param_1 = obj->addCar(carType);
 */