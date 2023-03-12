public class BinarizeForServer
{
    public static void main(String args[])
    {
        binarizeAndSave(args[0], args[1]);
    }
        
    public static void binarizeAndSave(String imagepath, String savepath)
    {
        Image srcimg = ImageUtility.readImage(imagepath);
        
        //## image setup
        float k = 0.25f;
        int w = 70;
        Binarization sauv = new Sauvola(k, w);
        sauv.setImage(srcimg);
        sauv.binarize();
        
        //perform open-close operation for preliminary noise removal
        Image openedImage = ImageUtility.open(sauv.getBinarizedImage(), 3);
        Image closedImage = ImageUtility.close(openedImage, 3);
        
        //save binarized image
        ImageUtility.writeImage(closedImage, savepath);
    }
}
