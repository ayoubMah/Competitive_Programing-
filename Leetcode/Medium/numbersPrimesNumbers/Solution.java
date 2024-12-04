/**
 * Determines whether the given integer is a prime number.
 *
 * @param a the integer to check for primality
 * @return true if the given integer is prime, false otherwise
 */
class Solution {
  public boolean isPrime(int a){
    if(a <= 1){
        return false;
    }
    if(a == 2){
        return true;
    }
    if(a % 2 == 0){
        return false;
    }
    // We only need to check up to square root of a because:
    // If a number n is not prime, it can be factored into n = a*b
    // If both a and b were greater than sqrt(n), then a*b would be greater than n
    // Therefore, at least one factor must be less than or equal to sqrt(n)
    for(int i = 3; i <= Math.sqrt(a); i += 2){
        if(a % i == 0){
            return false;
        }
    }
    return true;
  }
}