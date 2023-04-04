//------------------------------------------------------------------------------
// <auto-generated>
//     This code was generated by a tool.
//     Runtime Version:4.0.30319.42000
//
//     Changes to this file may cause incorrect behavior and will be lost if
//     the code is regenerated.
// </auto-generated>
//------------------------------------------------------------------------------

namespace Valve.VR
{
    using System;
    using UnityEngine;
    
    
    public partial class SteamVR_Actions
    {
        
        private static SteamVR_Action_Boolean p_zed_default_Grab;
        
        private static SteamVR_Action_Pose p_zed_default_Pose;
        
        private static SteamVR_Action_Vector2 p_zed_default_NavigateUI;
        
        private static SteamVR_Action_Boolean p_zed_default_Click;
        
        private static SteamVR_Action_Boolean p_zed_default_Back;
        
        private static SteamVR_Action_Boolean p_zed_default_Fire;
        
        private static SteamVR_Action_Vibration p_zed_default_Haptic;
        
        private static SteamVR_Action_Pose p_mixedreality_ExternalCamera;
        
        public static SteamVR_Action_Boolean zed_default_Grab
        {
            get
            {
                return SteamVR_Actions.p_zed_default_Grab.GetCopy<SteamVR_Action_Boolean>();
            }
        }
        
        public static SteamVR_Action_Pose zed_default_Pose
        {
            get
            {
                return SteamVR_Actions.p_zed_default_Pose.GetCopy<SteamVR_Action_Pose>();
            }
        }
        
        public static SteamVR_Action_Vector2 zed_default_NavigateUI
        {
            get
            {
                return SteamVR_Actions.p_zed_default_NavigateUI.GetCopy<SteamVR_Action_Vector2>();
            }
        }
        
        public static SteamVR_Action_Boolean zed_default_Click
        {
            get
            {
                return SteamVR_Actions.p_zed_default_Click.GetCopy<SteamVR_Action_Boolean>();
            }
        }
        
        public static SteamVR_Action_Boolean zed_default_Back
        {
            get
            {
                return SteamVR_Actions.p_zed_default_Back.GetCopy<SteamVR_Action_Boolean>();
            }
        }
        
        public static SteamVR_Action_Boolean zed_default_Fire
        {
            get
            {
                return SteamVR_Actions.p_zed_default_Fire.GetCopy<SteamVR_Action_Boolean>();
            }
        }
        
        public static SteamVR_Action_Vibration zed_default_Haptic
        {
            get
            {
                return SteamVR_Actions.p_zed_default_Haptic.GetCopy<SteamVR_Action_Vibration>();
            }
        }
        
        public static SteamVR_Action_Pose mixedreality_ExternalCamera
        {
            get
            {
                return SteamVR_Actions.p_mixedreality_ExternalCamera.GetCopy<SteamVR_Action_Pose>();
            }
        }
        
        private static void InitializeActionArrays()
        {
            Valve.VR.SteamVR_Input.actions = new Valve.VR.SteamVR_Action[] {
                    SteamVR_Actions.zed_default_Grab,
                    SteamVR_Actions.zed_default_Pose,
                    SteamVR_Actions.zed_default_NavigateUI,
                    SteamVR_Actions.zed_default_Click,
                    SteamVR_Actions.zed_default_Back,
                    SteamVR_Actions.zed_default_Fire,
                    SteamVR_Actions.zed_default_Haptic,
                    SteamVR_Actions.mixedreality_ExternalCamera};
            Valve.VR.SteamVR_Input.actionsIn = new Valve.VR.ISteamVR_Action_In[] {
                    SteamVR_Actions.zed_default_Grab,
                    SteamVR_Actions.zed_default_Pose,
                    SteamVR_Actions.zed_default_NavigateUI,
                    SteamVR_Actions.zed_default_Click,
                    SteamVR_Actions.zed_default_Back,
                    SteamVR_Actions.zed_default_Fire,
                    SteamVR_Actions.mixedreality_ExternalCamera};
            Valve.VR.SteamVR_Input.actionsOut = new Valve.VR.ISteamVR_Action_Out[] {
                    SteamVR_Actions.zed_default_Haptic};
            Valve.VR.SteamVR_Input.actionsVibration = new Valve.VR.SteamVR_Action_Vibration[] {
                    SteamVR_Actions.zed_default_Haptic};
            Valve.VR.SteamVR_Input.actionsPose = new Valve.VR.SteamVR_Action_Pose[] {
                    SteamVR_Actions.zed_default_Pose,
                    SteamVR_Actions.mixedreality_ExternalCamera};
            Valve.VR.SteamVR_Input.actionsBoolean = new Valve.VR.SteamVR_Action_Boolean[] {
                    SteamVR_Actions.zed_default_Grab,
                    SteamVR_Actions.zed_default_Click,
                    SteamVR_Actions.zed_default_Back,
                    SteamVR_Actions.zed_default_Fire};
            Valve.VR.SteamVR_Input.actionsSingle = new Valve.VR.SteamVR_Action_Single[0];
            Valve.VR.SteamVR_Input.actionsVector2 = new Valve.VR.SteamVR_Action_Vector2[] {
                    SteamVR_Actions.zed_default_NavigateUI};
            Valve.VR.SteamVR_Input.actionsVector3 = new Valve.VR.SteamVR_Action_Vector3[0];
            Valve.VR.SteamVR_Input.actionsSkeleton = new Valve.VR.SteamVR_Action_Skeleton[0];
            Valve.VR.SteamVR_Input.actionsNonPoseNonSkeletonIn = new Valve.VR.ISteamVR_Action_In[] {
                    SteamVR_Actions.zed_default_Grab,
                    SteamVR_Actions.zed_default_NavigateUI,
                    SteamVR_Actions.zed_default_Click,
                    SteamVR_Actions.zed_default_Back,
                    SteamVR_Actions.zed_default_Fire};
        }
        
        private static void PreInitActions()
        {
            SteamVR_Actions.p_zed_default_Grab = ((SteamVR_Action_Boolean)(SteamVR_Action.Create<SteamVR_Action_Boolean>("/actions/zed-default/in/Grab")));
            SteamVR_Actions.p_zed_default_Pose = ((SteamVR_Action_Pose)(SteamVR_Action.Create<SteamVR_Action_Pose>("/actions/zed-default/in/Pose")));
            SteamVR_Actions.p_zed_default_NavigateUI = ((SteamVR_Action_Vector2)(SteamVR_Action.Create<SteamVR_Action_Vector2>("/actions/zed-default/in/NavigateUI")));
            SteamVR_Actions.p_zed_default_Click = ((SteamVR_Action_Boolean)(SteamVR_Action.Create<SteamVR_Action_Boolean>("/actions/zed-default/in/Click")));
            SteamVR_Actions.p_zed_default_Back = ((SteamVR_Action_Boolean)(SteamVR_Action.Create<SteamVR_Action_Boolean>("/actions/zed-default/in/Back")));
            SteamVR_Actions.p_zed_default_Fire = ((SteamVR_Action_Boolean)(SteamVR_Action.Create<SteamVR_Action_Boolean>("/actions/zed-default/in/Fire")));
            SteamVR_Actions.p_zed_default_Haptic = ((SteamVR_Action_Vibration)(SteamVR_Action.Create<SteamVR_Action_Vibration>("/actions/zed-default/out/Haptic")));
            SteamVR_Actions.p_mixedreality_ExternalCamera = ((SteamVR_Action_Pose)(SteamVR_Action.Create<SteamVR_Action_Pose>("/actions/mixedreality/in/ExternalCamera")));
        }
    }
}
