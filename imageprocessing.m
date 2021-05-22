
rgbImage = imread('New folder/mask04.jpeg'); 
subplot(2,2,1);
grayImage = rgb2gray(rgbImage);
imshow(grayImage, []);
axis on;
subplot(2,2,2);
se = strel('disk', 4, 0);
filteredImage = imbothat(grayImage, se);
imshow(filteredImage, []);
axis on;
% Histogram
subplot(2,2,3);
histogram(filteredImage, 256);
grid on;
xticks(0:16:255);
% Threshold
binaryImage = filteredImage > 20;
subplot(2,2,4);
imshow(binaryImage);
particle_data = regionprops(binaryImage);
num_particles = numel(particle_data)

if num_particles < 500
    disp('It is clean enough, can be used for another time')
elseif 501 < num_particles<8000
  disp('The mask must be washed before further use!')
else
    disp('The mask is dirty to use, please discard')
end
