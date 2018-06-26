
//int  locate_clusters(int argc, void *argv[]);

int slit_func_vert(int ncols,           /* Swath width in pixels                                 */
                   int nrows,           /* Extraction slit height in pixels                      */
                   //int ny,              /* Size of the slit function array: ny=osample(nrows+1)+1*/
                   double *img,         /* Image to be decomposed                                */
                   int *mask, /* Initial and final mask for the swath                  */
                   double *ycen,        /* Order centre line offset from pixel row boundary      */
                   int osample,         /* Subpixel ovsersampling factor                         */
                   double lambda_sP,    /* Smoothing parameter for the spectrum, coiuld be zero  */
                   double lambda_sL,    /* Smoothing parameter for the slit function, usually >0 */
                   double *sP,          /* Spectrum resulting from decomposition                 */
                   double *sL,          /* Slit function resulting from decomposition            */
                   double *model,       /* Model constructed from sp and sf                      */
                   double *unc          /* Spectrum uncertainties                                */
);
