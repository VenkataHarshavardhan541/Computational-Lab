image_data = imread('2.jpg');

red_component = image_data(:,:,1);
green_component = image_data(:,:,2);
blue_component = image_data(:,:,3);

csvwrite('red_component.csv', red_component);
csvwrite('green_component.csv', green_component);
csvwrite('blue_component.csv', blue_component);

disp('Red, Green and Blue components of image saved in their respective csv files successfully');

