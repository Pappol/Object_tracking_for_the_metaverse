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
        
        private static SteamVR_Input_ActionSet_zed_default p_zed_default;
        
        private static SteamVR_Input_ActionSet_mixedreality p_mixedreality;
        
        public static SteamVR_Input_ActionSet_zed_default zed_default
        {
            get
            {
                return SteamVR_Actions.p_zed_default.GetCopy<SteamVR_Input_ActionSet_zed_default>();
            }
        }
        
        public static SteamVR_Input_ActionSet_mixedreality mixedreality
        {
            get
            {
                return SteamVR_Actions.p_mixedreality.GetCopy<SteamVR_Input_ActionSet_mixedreality>();
            }
        }
        
        private static void StartPreInitActionSets()
        {
            SteamVR_Actions.p_zed_default = ((SteamVR_Input_ActionSet_zed_default)(SteamVR_ActionSet.Create<SteamVR_Input_ActionSet_zed_default>("/actions/zed-default")));
            SteamVR_Actions.p_mixedreality = ((SteamVR_Input_ActionSet_mixedreality)(SteamVR_ActionSet.Create<SteamVR_Input_ActionSet_mixedreality>("/actions/mixedreality")));
            Valve.VR.SteamVR_Input.actionSets = new Valve.VR.SteamVR_ActionSet[] {
                    SteamVR_Actions.zed_default,
                    SteamVR_Actions.mixedreality};
        }
    }
}
