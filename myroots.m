% Finds the roots of a quadratic equation 
function myroots(a,b,c) 
posAns = (-b + sqrt(b^2 - 4 * a * c)) / (2 * a);
negAns = (-b - sqrt(b^2 - 4 * a * c)) / (2 * a);
disp("Estimated Results: ");
format long;
disp(posAns);
disp(negAns);
p = [a b c];
x = roots(p);
disp("Actual Results: ");
disp(x);
end