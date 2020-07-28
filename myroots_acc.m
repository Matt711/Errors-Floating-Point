function myroots_acc(a, b, c) 
posAns = -2 * c / (b + sqrt(b^2 - 4 * a * c));
negAns = (-b - sqrt(b^2 - 4 * a * c)) / (2 * a);
format long;
disp("Estimated Results: ");
disp(posAns);
disp(negAns);
p = [a b c];
x = roots(p);
disp(x)
end