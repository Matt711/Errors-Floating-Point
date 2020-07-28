x = .5;
u = -1:-1:-15;
h = 10 .^ u;
format long;
disp(h);
error1 = ((exp(x + h) - exp(x)) ./ h) - exp(x);
error2 = ((exp(x + h) - exp(x - h)) ./ (2 .* h)) - exp(x);
hold on;
plot(log(h), log(error1), 'r');
plot(log(h), log(error2), 'g');
hold off;
ax = gca; %Allows us to mess with the axes
ax.FontSize = 16; %Sets the fontSize to be readible