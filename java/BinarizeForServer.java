public class BinarizeForServer
{
    public static void main(String args[])
    {
        binarizeAndSave(args[0], args[1]);
    }
    
    public static void test()
    {
        binarizeAndSave("a.jpg", "tempqqa.jpg");
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
        
        Image dilatedImage = ImageUtility.dilate(sauv.getBinarizedImage(), 5);
        
        Segmentation segmentation = new Segmentation(dilatedImage);
        segmentation.segment();
        
        //save binarized image
        ImageUtility.writeImage(dilatedImage, savepath);
    }
}
