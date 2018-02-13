package net.clearcontrol.easyscopy.lightsheet.implementations.bscope;

import net.clearcontrol.lightsheet.easyscopy.EasyLightsheetMicroscope;
import net.clearcontrol.easyscopy.EasyScope;
import xwing.BScopeMicroscope;

import static com.esotericsoftware.minlog.Log.info;

/**
 * Author: Robert Haase (http://haesleinhuepf.net) at MPI CBG (http://mpi-cbg.de)
 * February 2018
 */
@EasyScope
public class BScope extends EasyLightsheetMicroscope
{
  public static boolean sUseStages = false;

  private static BScope sInstance = null;
  public static BScope getInstance() {
    if (sInstance == null) {
      sInstance = new BScope();
    }
    return sInstance;
  }

  private BScopeMicroscope mBScopeMicroscope;
  private BScope() {
    super(new BScopeBuilder(false).getBScopeMicroscope());
    mBScopeMicroscope = (BScopeMicroscope) getLightSheetMicroscope();
  }

  public static void cleanup() {
    if (sInstance != null) {
      sInstance.terminate();
      sInstance = null;
    }
  }





}
