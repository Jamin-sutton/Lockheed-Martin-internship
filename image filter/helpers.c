#include "helpers.h"
#include <stdio.h>
#include <math.h>


// BYTE  rgbtBlue BYTE  rgbtGreen; BYTE  rgbtRed;
// Convert image to grayscale
void grayscale(int height, int width, RGBTRIPLE image[height][width])
{
    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            RGBTRIPLE pixel = image[i][j];
            //find averager color value of rgb
           int average = ((pixel.rgbtBlue + pixel.rgbtGreen + pixel.rgbtRed) / 3.0)+0.5;

            //set all to same average
            pixel.rgbtBlue = average;
            pixel.rgbtGreen = average;
            pixel.rgbtRed = average;

            //reset original pixel
            image[i][j] = pixel;

        }
    }
    return;
}

// Reflect image horizontally
void reflect(int height, int width, RGBTRIPLE image[height][width])
{
    //switch i and width-i-1
    //adjusted width to go through row half of width -or- half of width plus one if odd
    int adjusted_width = (width/2)+0.5;

    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < adjusted_width; j++)
        {
            //getting values to swap
            RGBTRIPLE first_pixel = image[i][j];
            RGBTRIPLE second_pixel = image[i][width-j-1];
            //swapping
            image[i][width-j-1] = first_pixel;
            image[i][j] = second_pixel;


        }
    }
    return;
}

// Blur image
void blur(int height, int width, RGBTRIPLE image[height][width])
{
    RGBTRIPLE new_image[height][width];

    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            int r_all = 0;
            int g_all = 0;
            int b_all = 0;
            int divider = 0;
            RGBTRIPLE pixel;
            //getting pixel then finding all pixels touching that pixel
            for (int h = i - 1; h <= (i + 1); h++)
            {
                if (h < 0 || h >= height)
                {
                    continue;
                }
                for (int w = j - 1; w <= (j + 1); w++)
                {
                    if (w < 0 || w >= width)
                    {
                        continue;
                    }
                    pixel = image[h][w];
                    r_all += pixel.rgbtRed;
                    g_all += pixel.rgbtGreen;
                    b_all += pixel.rgbtBlue;
                    divider++;

                }
            }
            //making new pixel in new image arr
            //averaging all pixel vals in one line--> i was lazy and didn't feel like making it easy to read
            RGBTRIPLE new_pixel = {((int)(b_all/divider)+0.5),((int)(g_all/divider)+0.5),((int)(r_all/divider)+0.5)};
            new_image[i][j] = new_pixel;
        }
    }

    //copying new image into image
    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            image[i][j] = new_image[i][j];
        }
    }
    return;
}


//calc root of Gx^2+Gy^2
int calc_G(int gx, int gy)
{
    int MAX = 255;
    int total = sqrt(pow(gx, 2) + pow(gy, 2)) + 0.5;

    if (total > MAX)
    {
        return MAX;
    }
    return total;
}



// Detect edges
void edges(int height, int width, RGBTRIPLE image[height][width])
{
    //convolutioanl change matrixes: mult this to surroudning pixels to find change in edges
    int gx_matrix[3][3] = {{-1, 0, 1}, {-2, 0, 2}, {-1, 0, 1}};
    int gy_matrix[3][3] = {{-1, -2, -1}, {0, 0, 0}, {1, 2, 1}};
    //new image for copying//
    RGBTRIPLE  new_image[height][width];


    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            int r_x = 0;
            int g_x = 0;
            int b_x = 0;

            int r_y = 0;
            int g_y = 0;
            int b_y = 0;
            int divider = 0;
            RGBTRIPLE pixel;
            //getting pixel then finding all pixels touching that pixel
            int matrix_i = 0;
            for (int h = i - 1; h <= (i + 1); h++)
            {

                if (h < 0 || h >= height)
                {
                    matrix_i++;
                    continue;
                }
                int matrix_j = 0;
                for (int w = j - 1; w <= (j + 1); w++)
                {
                    if (w < 0 || w >= width)
                    {
                        matrix_j++;
                        continue;
                    }
                    pixel = image[h][w];
                    r_x += pixel.rgbtRed * gx_matrix[matrix_i][matrix_j];
                    g_x += pixel.rgbtGreen * gx_matrix[matrix_i][matrix_j];
                    b_x += pixel.rgbtBlue * gx_matrix[matrix_i][matrix_j];

                    r_y += pixel.rgbtRed * gy_matrix[matrix_i][matrix_j];
                    g_y += pixel.rgbtGreen * gy_matrix[matrix_i][matrix_j];
                    b_y += pixel.rgbtBlue * gy_matrix[matrix_i][matrix_j];

                    matrix_j++;
                }
                matrix_i++;
            }
            //making new pixel in new image arr
            //setting new pixel to val
            RGBTRIPLE new_pixel = {calc_G(b_x, b_y), calc_G(g_x, g_y), calc_G(r_x, r_y)};
            new_image[i][j] = new_pixel;
        }
    }

    //copying new image into image//
    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            image[i][j] = new_image[i][j];
        }
    }

    return;
}
